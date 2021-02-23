# LowResourceLanguages
Project devoted to investigation of strategies for the improvement of low-resourced Machine Translation. [Joeynmt](https://github.com/joeynmt/joeynmt) was used as a tool for training MT systems.

## Ky-Ru data
Ky-Ru data is represented by 334508 parallel sentences collected mostly from [OPUS](http://opus.nlpl.eu/) and preprocessed by [MOSES](http://www.statmt.org/moses/).

## Lez-Ru data
Lez-Ru data is represented by 7757 parallel sentences collected in a manual manner.

## Usage

### Pre-processing

The [MOSES](http://www.statmt.org/moses/) toolkit provides a set of useful scripts for this purpose. 

Having installed MOSES preprocessing can be done via:

`bash /src/scripts/preprocessing.sh /src/mosesdecoder/ /data/data/ train lez ru`


### Joeynmt installation and usage.
Joey NMT is built on [PyTorch](https://pytorch.org/) and [torchtext](https://github.com/pytorch/text) for Python >= 3.5.
  1. Clone this repository:
  `git clone https://github.com/joeynmt/joeynmt.git`
  2. Install joeynmt and it's requirements:
  `cd joeynmt`
  `pip3 install .` (or `python3 -m pip install .`).
  
 For training, run:
 
 `python3 -m joeynmt train configs/lez_ru_baseline.yaml`.
  
 For testing on your parallel test set, run:
 
`python3 -m joeynmt test configs/lez_ru_baseline.yaml --output_path out`.

## Current results (BLEU)

| Pair  | Baseline | MOSES | Transformer | LaBSE | LSTM for augmentation | Additional turkish cyrillized corpus (~250k) | Additional turkish cyrillized corpus (~450k) | Additional morfessed turkish cyrillized corpus (~250k) | Additional morfessed turkish cyrillized corpus (ky also morfessed) (~250k) | GPT2-Fine tuned |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Ky-Ru  | 12.67±0.18   | 13.30 | 11.77  |14.98±0.28   | 13.06±0.35 | 13.25 | 12.79 | 12.42 | 11.67 | 15.39
| Lez-Ru  | 3.21±0.35  | 6.53 | 3.25 |2.61±0.14 | 1.94±0.28 | - | - | - | - | 7.08

| Pair  | BPE merge | BLEU
| ------------- | ------------- | ------------- |
| Lez-Ru | 100  | 1.92 |
| Lez-Ru | 200   | 1.59 |
| Lez-Ru | 400   | 2.75 |
| Lez-Ru | 1000   | 1.67 |
| Lez-Ru | 5000   | 1.100 |
| Lez-Ru | 10000   | 0.71 |

| ky-ru parallel sents  | BLEU
| ------------- | ------------- |
| 150k | 15.39 |
| 100k | 13.89 |
| 75k | 12.49 |
| 30k | 8.88 |


### Chain traslators with turkish

| Pair  | BLEU | 
| ------------- | ------------- |
| Ky_Ru + Tr_Ru + Rub_Rug  | 0.11   |
| Ky_Ru + Tr_Ru + Rub_Rug_Bible  | 0.10  |
