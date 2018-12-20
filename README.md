# F039-1_AJ_Intensive
2018 Intensive Course for Ajou University_DL

# T.T.T.S
**T**ranslated korean **T**ext **T**o **S**peech
> Bootstrapped with [Kyubyong/kss](https://github.com/Kyubyong/kss)

## How to Start
1. Clone this project and checkout to remote branch **Group3**
    ```bash
    $ git clone https://github.com/songhune/F039-1_AJ_Intensive/
    $ cd F039-1_AJ_Intensive
    $ git remote update
    $ git checkout -t origin/Group3
    ```
2. Get into **group3** Folder
    ```bash
    $ cd group3
    ```
3. Run
   ```bash
   $ pip install -r requirements.txt # (Python 2)
   ```
   or
   ```bash
   $ pip install -r requirements.txt # (Python 3)
   ```
   to install all dependencies
4. Download **Model Pretrained with ```num_exp=0```** From [Here](https://www.dropbox.com/s/ipt17hoo4lj56xg/exp0.zip?dl=0)
5. Unzip downloaded and rename unzipped **exp0** folder to **logdir**
6. Locate it to **group3** folder. Your project folder will appear like this
    ```bash
    .
    └── F039-1_AJ_Intensive
        └── group3
            └── logdir
                ├── 0-1
                └── 0-2
    ```

    
## Test **Translated Text to Speech**
1. Get API Keys from Naver *papago* API KEY, PASSWORD from *[Naver Developer](https://developers.naver.com/products/nmt/)*
2. insert your API Key and Password to **synthesis.py** like this
    ```python
    client_id = ""  # 자신이 제공 받은 KEY ID
    client_secret = ""  # 자신이 제공 받은 KEY 암호
    ```
3. Run `python synthesis.py` in group3 folder
4. type english sentence to translated when something appears like this
    ```bash
    > Text to Speech : 
    ```
5.  After logs of synthesis, a *wav* file will created like this
    ```bash
    .
    └── F039-1_AJ_Intensive
        └── group3
            └── samples
                └── 0
                    └── 1.wav
    ```
    
## Test **Korean Alphabetizer**
1. Edit `test_keyword` in **hangul-alphabetizer.py**
    ```python
    test_keyword = "이러지도 못하는데"
    ```
2. run `python hangul-alphabetizer.py`, then distributed 'Hangul Jamo' will appear like this
    ```bash    
    ['이', '러', '지', '도', ' ', '못', '하', '는', '데']
    이러지도 못하는데
    ```

## Team 3 members
* 이정은, 201420980 [ijsilver](https://github.com/ijsilver)
* 이충희 201420919, [ChUngHEe0227](https://github.com/ChUngHEe0227)
* 방성호, 201320891, [crosstreet74](https://github.com/crosstreet74)
