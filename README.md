# F039-1_AJ_Intensive
# 2018 Intensive Course for Ajou University_DL
# Ajou University
## Department of Software

## Intensive Course
## Team Project #3

mid due: 16  December 2018
final due: 21 December 2018




### 1. 프로젝트 목표

- 딥러닝 메커니즘과 그 접근법을 소개한다.
- 학생들이 Tensorflow 프레임워크를 설치하고 실행하도록 조장한다.
- 파이썬 언어를 사용하여 학생 자연어 응용 프로그램을 개발한다.
- NLP 작업을 수행하기 위해 학생의 종단 간 모델을 구현하는 법을 소개한다.

### 2. 프로젝트 설명

자연어 처리 (NLP)는 정보 시대의 가장 중요한 기술 중 하나입니다. 언어 모델의 복잡성을 이해하는 것은 인공 지능의 중요한 부분이기도합니다. 사람들이 자연어로 의사 소통하기 때문에 NLP의 응용 프로그램은 거의 모든 곳에서 이루어집니다 : 웹 검색, 광고, 이메일, 번역 등. 최근 심층 학습 접근법의 재창조에 의한 NLP 작업의 상당한 개선이 단일 종단 간 모델을 통해 다양한 NLP 작업을 해결할 수 있습니다. 이 프로젝트는 학생들에게 자신의 신경망 모델을 구현, 훈련, 디버그, 시각화 및 발명할 수 있도록합니다.  
이 프로젝트에서는 상당한 백본 아키텍처를 가진 각 그룹에 5 개의 프로젝트 작업이 제공됩니다. 그룹이 제안된 작업을 만족시키지 못하면 코스 강사와의 확인 후 자신의 NLP 작업을 선택할 수 있습니다. 다음은 간단한 설명이 포함된 프로젝트 작업입니다.  
- Word prediction  
- Chinese Pinyin to Chinese letters  
- Roman expression Japanese to Kana  
- Making TTS with his voice  
- Finding similar voice with me  


### 3. 발표물
- 발표자료  
중간 presentation – 16 Dec 2018  
최종 presentation – 21 Dec 2018  
소스코드 (Github): 최종발표일까지  
최종보고서t: 학기말까지 (21 Dec 2018)  
학생들은 자신의 과제에 대한 설명을 포함하여 모델을 보여주거나 시연해야 합니다

### 4. 평가
- 텐서플로우 플로우
- 각 팀 구성원의 기여 부분
- 현 무결성 및 문서 상세 정보
- 실험 결과
- 피어 평가가 포함된 프리젠테이션 자료입니다.

#### Postscript
너무 크지 않은 딥러닝 프로젝트를 바탕으로 프로젝트를 4~5개정도 미리  추천할까 합니다. 저는 언어 쪽 외에는 잘 몰라서 대부분 언어 관련 프로젝트들입니다. 제가 한 (파일럿) 프로젝트들과 많이 엮여 있는데 저는 제 식대로 한 게 많아서 사실 각자 자기 식대로 주제를 디자인할 수 있습니다. 본 프로젝트는 제가 있는 커뮤니티(TFKorea)의 멤버 박규병님의 프로젝트를 기초로 합니다. 물론, 모든 프로젝트는 오픈소스이므로 저작상의 문제는 전혀 없습니다.
1. Word prediction (https://github.com/Kyubyong/word_prediction 참고)
언어 모델은 nlp의 101이고 그 자체로 응용되는 분야가 현재/다음 단어를 얼마나 잘 예측하느냐 하는 것입니다. 모바일 키보드의 성능 평가 요소 중 하나기도 한 이 프로젝트는 실력이 가장 떨어지는 팀이 하기에 좋을 것 같습니다.
2. 중국어 병음 to 한자 변환 (https://github.com/Kyubyong/neural_chinese_transliterator 참고)
중국어 표기 문자인 한자는 표음 문자가 아니라서 병음이라 불리는 로마자를 이용해 입력합니다. 키보드의 내장 엔진은 병음을 한자로 변환해 반환하는데 이 정확도가 매우 중요한 요소입니다. 저는 온라인에서 데이터를 긁어 만들고, 제 마음대로 테스트셋을 구축도 하고 다른 키보드 모델 타이핑을 직접 해서 성능 비교를 했었습니다. 본인의 아이디어로 이 프로젝트를 훨씬 발전시킬 부분이 있을 겁니다. 참고로 pinyin to chinese 라는 쿼리로 검색해 보면 관련 논문도 꽤 있습니다.
3. 일본어 로마지 to [가나/한자] 변환 (https://github.com/Kyubyong/neural_japanese_transliterator 참고)
중국어랑 비슷한 컨셉입니다. 몇 달 전 나고야의 한 대학원생으로부터 이 레포를 참고해서 논문을 쓰고 있다는 연락을 받았습니다. 일본어에 관심이 있는 팀이 있다면 마찬가지로 연구 주제로 삼아볼 만합니다.
4. 자기 목소리로 TTS 만들기 (https://github.com/Kyubyong/tacotron, https://github.com/Kyubyong/dc_tts, https://github.com/Kyubyong/kss 참고)
음성에 관심이 있다면 TTS를 직접 만들어 보는 것도 의미가 있을 것 같습니다. 이미 잘 정리된 데이터셋이 있지만 자기 목소리를 학습 데이터로 해서 모델을 만들어 봐도 재밌을 거 같아요. 일단 한 시간 정도 녹음한 뒤 모델을 학습시켜 보고 추가로 한 시간 한 뒤 추가 학습시켜 성능을 비교해 보면 어떨까 합니다. 제가 예전에 참여했었던 프로젝트는 유튜브에서 전/현임 대통령 목소리를 크롤링하여 그 목소리를 만들어내는 작업을 했습니다. 찾아보면 참고로 할 수 있는 더 좋은 코드들이 많습니다.
5. 나와 비슷한 유명인 목소리 찾아주기 (https://github.com/andabi/voice-vector 참고)
본 small project를 기획한 박규병님과 브레인의 안다비 님이 주도적으로 진행한 프로젝트입니다. 많은 유명인의 목소리 샘플들에서 voice vector를 학습하고 그에 따라 임의의 입력이 들어오면 그와 가장 가까운 목소리를 찾아 들려주는 컨셉의 프로젝트로 데모도 있으니 한번 해 보시면 재밌을 것 같습니다. 성능이 완벽하지 않아 때로는 안 비슷한 거 같다는 피드백도 많았어요. speaker recognition, speaker embedding 등의 태스크와 관련이 깊습니다. 
QA task(question answering task)나, Visual QA, Machine Translation등도 해당 그룹이 원한다면 수행할 수 있도록 할 것 같습니다. 평가는 다른 팀과 마찬가지로 document와 presentation으로 수행할 예정입니다. 
