# LowResourceLanguages
Project devoted to investigation of strategies for the improvement of low-resourced Machine Translation. [Joeynmt](https://github.com/joeynmt/joeynmt) was used as a tool for training MT systems.

## Ky-Ru data
Ky-Ru data is represented by 334508 parallel sentences collected mostly from [OPUS](http://opus.nlpl.eu/) and preprocessed by [MOSES](http://www.statmt.org/moses/).

## Lez-Ru data
Lez-Ru data is represented by 7757 parallel sentences collected in a manual manner.


## Joeynmt installation and usage.
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

### Current results (BLEU)

| Pair  | Baseline | Pbsmt | LaBSE | LSTM for augmentation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Ky-Ru  | 12.67±0.18   | 6.83 | 14.98±0.28   | 13.06±0.35 |
| Lez-Ru  | 3.21±0.35  | 0.76 | 2.61±0.14 | 1.94±0.28 |

| Pair  | BPE merge | BLEU
| ------------- | ------------- | ------------- |
| Lez-Ru | 100  | 1.92 |
| Lez-Ru | 200   | 1.59 |
| Lez-Ru | 400   | 2.75 |
| Lez-Ru | 1000   | 1.67 |
| Lez-Ru | 5000   | 1.100 |
| Lez-Ru | 10000   | 0.71 |


### Chain traslators with turkish

| Pair  | BLEU | 
| ------------- | ------------- |
| Ky_Ru + Tr_Ru + Rub_Rug  | 0.11   |
| Ky_Ru + Tr_Ru + Rub_Rug_Bible  | 0.10  |
