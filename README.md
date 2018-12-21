# F039-1_AJ_Intensive
## Team Members

*  201621048 신희수 [effya](https://github.com/effya)
*  201620923 정다원 [DawonJeong](https://github.com/DawonJeong)
*  201321019 권태성 [TaesungKwon](https://github.com/TaesungKwon)

## About Project

현재의 디지털 환경에서 사람들은 Roman alphabet을 통해 일본어를 입력한다. 따라서 번역 엔진이 얼마나 사용자가 원하는 단어를 잘 예측하는가가 중요하다. 이에 이번 프로젝 트에서는 뉴럴 네트워크가 알파벳을 일본어 스크립트로 얼마나 잘 변환할 수 있는 가를 살펴본다.

## Requirements
* NumPy >= 1.11.1
* TensorFlow == 1.2
* regex (Enables us to use convenient regular expression posix)
* janome (for morph analysis)
* romkan (for converting kana to romaji)

## Related Concepts
* RNN
* beam search

## How to operate(기존 프로젝트 실행법)
### Training

* STEP 1. [Leipzig Japanese Corpus](http://corpora2.informatik.uni-leipzig.de/download.html)를 다운로드 받고,`jpn_news_2005-2008_1M-sentences.txt`파일을 `data/` folder에 압축해제한다.
* STEP 2. 필요하다면,`hyperparams.py`의 하이퍼 파라미터를 조정한다.
* STEP 3. `python annotate.py`를 실행시킨다.
* STEP 4. `python prepro.py`를 실행시킨다.
* STEP 5. `train.py`를 실행시킨다.

### Testing

* STEP 1. `eval.py`를 실행시킨다.
* STEP 2. 스위프트 키보드 앱을 다운로드 받아 같은 문장에 대해 테스트한다.(기존 프로젝트 안에 이미 해당 결과물이 존재한다)

### How to operate our project
* `hyperparams.py`의 하이퍼 파라미터를 조정한다.
* [preprocessed files](https://www.dropbox.com/s/tv81rxcjr3x9eh1/preprocessed.zip?dl=0)를 다운로드한다. 그리고 STEP 4 대신, 다운로드 받은 파일을 프로젝트폴더 안에 압축해제한다.
* [pretrained files(trained 13 times)](https://www.dropbox.com/s/wrbr7tnf4zva4bj/logdir.zip?dl=0) 또는 [pretrained files(trained 1 times)](https://drive.google.com/file/d/1V8cHEEq6gMgEKQBKT7_4C3zNy-1HSloE/view?usp=sharing)를 다운로드 받는다. 그리고 STEP 5 대신, 다운로드 받은 파일을 프로젝트폴더 안에 압축해제한다.
* `eval.py`를 실행시킨다.

## How did we improve
`hyperparams.py`의 Beam_width 의 값을 조정하며 나온 결과값들을 비교하였다. 결과물들은 `/images` 폴더 안에서 확인할 수 있다. train 횟수와 beam 길이별로 폴더가 나뉘어 있다.

## Conclusion
컴퓨터의 성능때문에 학습뿐만 아니라 결과 평가에 있어서도 많은 시간이 소요되었다. 좋은 성능의 컴퓨터를 사용하여 다양한 평가들을 얻은 뒤 많은 데이터를 바탕으로 결과를 도출해내고 싶었는데 그렇게까지 못해서 아쉬움이 남았다. 다만 프로젝트를 진행하며 머신러닝의 개요와 기초지식에 대해 파악할 수 있다는 점에 의의를 두고 싶다. 기회가 된다면 error rate를 더욱 더 낮출 수 있는 방법을 모색하여 적용해보고 싶다.
