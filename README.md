# F039-1_AJ_Intensive
2018 Intensive Course for Ajou University_DL

## 1. 조원
----------
* 이다운 201420983 rhdrlvnd
* 김동현 201420981 ehgus6260
* 박준혁 201620940 YouDaHe

## 주제
-------
* Making TTS with his voice


## Training
  * STEP 0. Download [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/) or prepare your own data.
  * STEP 1. Adjust hyper parameters in `hyperparams.py`. (If you want to do preprocessing, set `prepro` True`.
  * STEP 2. Run `python train.py`. (If you set `prepro` True, run `python prepro.py` first)
  * STEP 3. Run `python eval.py` regularly during training.

## Sample Synthesis

We generate speech samples based on [Harvard Sentences](http://www.cs.columbia.edu/~hgs/audio/harvard.html) as the original paper does. It is already included in the repo.

  * Run `python synthesize.py` and check the files in `samples`.
