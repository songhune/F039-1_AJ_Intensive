# F039-1_AJ_Intensive
2018 Intensive Course for Ajou University_DL
## 1팀
* 최지원, 201420997, [ChoeJiwon](https://github.com/ChoeJiwon)
* 김상호, 201620979, [hol819](https://github.com/hol819)
* 최혜지, 201620933, [chj777](https://github.com/chj777)

## 주제
* Word_Prediction

## Installation

* Basic Setting: Git Clone을 한 후에 환경설정을 해주어야 한다. Requirements는 다음과 같다.
- numpy >= 1.11.1
- sugartensor >= 0.0.2.4
- lxml >= 3.6.4.
- nltk >= 3.2.1.
- regex
* ***주의***: 위 requirements는 기존 프로그램에서 요구되어진 환경설정으로, 만약 최신 버젼으로 pip install을 할 경우에는 함수의 파라미터가 다르기 때문에 오류가 발생할 수 있다.

## Work Flow(실제로 사용하지 않음)

* STEP 1. 해당 사이트에 들어가서 데이터를 다운로드 한다. [English wikinews dumps](https://dumps.wikimedia.org/enwikinews/20170120/).
* STEP 2. xml파일로 되어있는 output을 `data/raw`폴더 안에 복사한다.
* STEP 3. 'build_corpus.py' 을 실행한다. 이를 통해 enwikinews.txt가 생성된다면 성공이다. 
* STEP 4. `prepro.py` 을 실행한다. 이를 통해 vocabulary 와 training/test 데이터가 만들어진다면 성공이다.
* STEP 5. `train.py` 을 실행한다.
* STEP 6. `eval.py` 을 실행한다. output_{}_rk_{}.csv 파일이 생성된다면 성공이다.
* STEP 7. 이를 아이폰 7의 자동 완성 기능과 비교해본다. (이는 매우 번거로운 작업으로 본 프로젝트에서는 다음 pretrained model을 사용하였다.)

## You should follow these WorkFlow. 

* STEP 1. 해당 사이트에 들어가서 파일을 다운로드 한 후, 'data/' 폴더 안에 복사한다.
=> *https://drive.google.com/open?id=0B0ZXk88koS2KemFWdFNoSnBfNDg* 
* SETP 2. 해당 사이트에서 파일을 다운로드 한 후 `asset/train`폴더 안에 복사한다.    => *https://drive.google.com/open?id=0B0ZXk88koS2KNHBuM09kSXFJNzA*
* `eval.py` 을 실행한다. 위 Work Flow와 같이 output_{}_rk_{}.csv 파일이 생성된다면 성공이다.

## Changes of Project

* prepro.py 파일안의 HyperParams.seqlen을 50->60으로 바꿔주었다.

## Result

* 기존 프로젝트에서 얻었던 결과값보다 성능이 0.00068% 향상되었다.

## Conclusion

* 모듈의 버젼이 계속 업데이트 되면서 본 프로젝트의 실행 환경과 기존 프로젝트의 실행 환경이 달라졌고, 이에 따라 프로그램이 제대로 실행되지 않는 결과가 발생하였다. 이를 해결하기 위해서는 기존 프로젝트의 모든 환경설정을 가져와 그대로 따라해야 하나, 시간이 부족한 관계로 하지 못하였다.
* 위에서 말한 것과 같이 프로그램이 제대로 실행되지 않았으며 특히 train.py에서 오류가 많이 발생하였다. 기존 프로젝트에서 Architecture Model과 HyperParams, learning rate을 바꾸기 위해서는 train.py 에서도 설정을 바꾸어 주어야 하는데 이 또한 시간 문제로 해결하지 못하였다.
* 결론적으로 시간이 많이 모자라 제대로 해보지 못한 시도들이 많다. 또한 팀원 중 랩탑에 GPU가 내장되어 있지 않아 CPU로 프로그램을 돌리다 보니 매우 많은 시간이 들었다.
* HyperParams.seqlen을 60으로 바꿔 기존 프로그램보다 매우 작은 향상이 이루어졌다는 것에 대해 이번 프로젝트의 의의를 두고, 딥러닝에 대해 매우 기초적인 지식을 쌓기 좋은 기회였다고 생각한다.