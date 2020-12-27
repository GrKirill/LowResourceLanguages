import os
from tqdm import tqdm
import subprocess
import io
import json
import sys

def modify_ini(path_to_moses_ini):
    modified = []
    with open(path_to_moses_ini, 'r') as f:
        for line in f:
            if (line.split(" ")[0] == 'PhraseDictionaryMemory'):
                modified.append('PhraseDictionaryCompact ' + 'name=TranslationModel0 num-features=4 path=' + '/data/phrase-table-pruned ' + 'input-factor=0 output-factor=0')
                continue
            if (line.split(" ")[0] == 'LexicalReordering'):
                modified.append('#'+line)
                continue
            if (line.split(" ")[0] == 'LexicalReordering0='):
                modified.append('#'+line)
                continue
            else:
                modified.append(line)    

    with open(path_to_moses_ini, 'w') as f:
        for line in modified:
            f.write(line)
    return path_to_moses_ini
   

all_files = os.listdir('/data/Translators')
all_lang_dirs = []
for file in tqdm(all_files):
    to_check = '/data/Translators/' + file
    if (os.path.isdir(to_check)==True) and file!='.ipynb_checkpoints':
        all_lang_dirs.append(file)


dirs_moses_1 = ['ky_ru']


working_dir = sys.argv[1:]   
print(working_dir)
if working_dir[0]=='1':
    dirs = dirs_moses_1
    proc = ['0','4']


for file in dirs:
    print(file)
    lang_1 = file.split('_')[0]
    lang_2 = file.split('_')[1]
    run_moses = "sudo docker run --name moses" + "_"+ proc[0] + "_" + proc[1] + " -d --cpuset-cpus=" + proc[0] + "-" + proc[1] + " -v /data/Translators/"+ lang_1 +'_'+ lang_2 + "/:/data -v /src/scripts:/src/scripts moses-translate sleep 9999999999"
    os.system(run_moses)
    cleaning_train = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/preprocessing.sh /src/mosesdecoder/ /data/data/ prep_train " + lang_1 + " " + lang_2  #
    cleaning_valid = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/preprocessing.sh /src/mosesdecoder/ /data/data/ prep_valid " + lang_1 + " " + lang_2
    cleaning_test = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/preprocessing.sh /src/mosesdecoder/ /data/data/ prep_test " + lang_1 + " " + lang_2
    os.system(cleaning_train)
    os.system(cleaning_valid)
    os.system(cleaning_test)
    language_model = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/language_model.sh /src/mosesdecoder/ /data/ /data/data/ prep_train.tok " +  lang_2
    os.system(language_model)
    translator = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/moses_learning.sh /src/mosesdecoder/ /data/ /data/data/ prep_train.tok " + lang_1 + " " + lang_2
    os.system(translator)
    pruning = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/prune.sh /src/mosesdecoder/ /data/train/model/ /data/data/ prep_train.tok " + lang_1 + " " + lang_2
    os.system(pruning)
    binarization = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " /src/mosesdecoder/bin/processPhraseTableMin -in /data/train/model/phrase-table.pruned.gz -nscores 4 -out /data/phrase-table-pruned"
    os.system(binarization)
    path_to_ini = '/data/Translators/' + file + '/train/model/moses.ini'
    os.chmod(path_to_ini, 777)
    modify_ini(path_to_ini)
    mert = "sudo docker exec -it moses" + "_"+ proc[0] + "_" + proc[1] + " bash /src/scripts/mert.sh /src/mosesdecoder/ /data/train/model/moses.ini /data/ /data/data/ prep_valid.tok " + lang_1 + " " + lang_2
    os.system(mert)
    remove_container = "sudo docker rm -f moses" + "_" + proc[0] + "_" + proc[1]
    os.system(remove_container)