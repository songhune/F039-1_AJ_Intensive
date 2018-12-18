# -*- coding: utf-8 -*-
# /usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/multi-speech-corpora/dc_tts
'''

from __future__ import print_function

import os
import urllib.request
from hyperparams import Hyperparams as hp
import numpy as np
import tensorflow as tf
from train import Graph
from utils import *
from data_load import new_load_data
from scipy.io.wavfile import write
from tqdm import tqdm
import json

# Naver Papago API Key
client_id = ""  # 자신이 제공 받은 KEY ID
client_secret = ""  # 자신이 제공 받은 KEY 암호
url = "https://openapi.naver.com/v1/papago/n2mt"


def synthesize(ko_txt):
    # Load data
    L = new_load_data(ko_txt, "synthesize")

    # Load graph
    g = Graph(mode="synthesize")
    print("Graph loaded")

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        # Restore parameters
        var_list = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
                                     'Text2Mel')
        saver1 = tf.train.Saver(var_list=var_list)
        saver1.restore(sess, tf.train.latest_checkpoint(hp.logdir + "-1"))
        print("Text2Mel Restored!")

        var_list = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, 'SSRN') + \
                   tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, 'gs')
        saver2 = tf.train.Saver(var_list=var_list)
        saver2.restore(sess, tf.train.latest_checkpoint(hp.logdir + "-2"))
        print("SSRN Restored!")

        # Feed Forward
        ## mel
        Y = np.zeros((len(L), hp.max_T, hp.n_mels), np.float32)
        prev_max_attentions = np.zeros((len(L), ), np.int32)
        for j in tqdm(range(hp.max_T)):
            _gs, _Y, _max_attentions, _alignments = \
                sess.run([g.global_step, g.Y, g.max_attentions, g.alignments],
                         {g.L: L,
                          g.mels: Y,
                          g.prev_max_attentions: prev_max_attentions})
            Y[:, j, :] = _Y[:, j, :]
            prev_max_attentions = _max_attentions[:, j]

        # Get magnitude
        Z = sess.run(g.Z, {g.Y: Y})

        # Generate wav files
        if not os.path.exists(hp.sampledir): os.makedirs(hp.sampledir)
        for i, mag in enumerate(Z):
            print("Working on file", i + 1)
            wav = spectrogram2wav(mag)
            write(hp.sampledir + "/{}.wav".format(i + 1), hp.sr, wav)

if __name__ == '__main__':
    ko_txt = input('> Text to Speech : ')
    encText = urllib.parse.quote(ko_txt)
    data = "source=en&target=ko&text=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        res_text = response_body.decode('utf-8')
        res_obj = json.loads(res_text)
        translated = res_obj['message']['result']['translatedText']
        print(translated)
        ko_txt = translated
        ko_txt.replace("\n", "")
        ko_txt = ko_txt + "|" + ko_txt + "|" + ko_txt
        synthesize(ko_txt)
    else:
        print("error")
        print("Error Code:" + rescode)

    print("Done")
