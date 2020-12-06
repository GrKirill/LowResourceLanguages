# LowResourceLanguages
Project devoted to investigation of strategies for the improvement of low-resourced Machine Translation

## Ky-Ru data
Ky-Ru data is represented by 334508 parallel sentences collected mostly from OPUS(http://opus.nlpl.eu/) and preprocessed by MOSES(http://www.statmt.org/moses/).

## Lez-Ru data
Lez-Ru data is represented by 7757 parallel sentences collected in a manual manner.

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
