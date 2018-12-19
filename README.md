# F039-1_AJ_Intensive
## Team Members

*  201621048 신희수 [effya](https://github.com/effya)
*  201620923 정다원 [DawonJeong](https://github.com/DawonJeong)
*  201321019 권태성 [TaesungKwon](https://github.com/TaesungKwon)

## About Project

## Requirements
* NumPy >= 1.11.1
* TensorFlow == 1.2
* regex (Enables us to use convenient regular expression posix)
* janome (for morph analysis)
* romkan (for converting kana to romaji)

## Related Concepts
RNN, beam search

## How to operate
### Training

* STEP 1. Download [Leipzig Japanese Corpus](http://corpora2.informatik.uni-leipzig.de/download.html). and extract `jpn_news_2005-2008_1M-sentences.txt` to `data/` folder.
* STEP 2. Adjust hyperparameters in `hyperparams.py` if necessary.
* STEP 3. Run `python annotate.py`.
* STEP 4. Run `python prepro.py`.
* STEP 5. Run `train.py`.

### Testing

* STEP 1. Run `eval.py`.
* STEP 2. Install the latest SwiftKey keyboard app and manually test it for the same sentences. (Don't worry. You don't have to because I've done it:))

### if you want to use the pretrained model,
* Download [preprocessed files](https://www.dropbox.com/s/tv81rxcjr3x9eh1/preprocessed.zip?dl=0). of STEP 4, then extract them to your project folder.
* Download [pretrained files(trained 13 times)](https://www.dropbox.com/s/wrbr7tnf4zva4bj/logdir.zip?dl=0) or [pretrained files(trained 1 times)](https://drive.google.com/file/d/1V8cHEEq6gMgEKQBKT7_4C3zNy-1HSloE/view?usp=sharing). of STEP 5, then extract them to your project folder.
* Run `eval.py`.

## How did we improve
빔 서치 통해서 결과 improve된 것 보여주기

## Conclusion

