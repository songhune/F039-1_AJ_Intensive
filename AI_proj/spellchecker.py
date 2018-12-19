from __future__ import print_function

from hyperparams import Hyperparams as hp
from autocorrect import spell
import numpy as np
import tensorflow as tf
from utils import *
import codecs
import re
import os
import unicodedata

def load_vocab():
    char2idx = {char: idx for idx, char in enumerate(hp.vocab)}
    idx2char = {idx: char for idx, char in enumerate(hp.vocab)}
    return char2idx, idx2char

def text_normalize(text):
    text = ''.join(char for char in unicodedata.normalize('NFD', text)
                           if unicodedata.category(char) != 'Mn') # Strip accents

    text = text.lower()
    text = re.sub("[^{}]".format(hp.vocab), " ", text)
    text = re.sub("[ ]+", " ", text)
    return text

def spell_check():
    char2idx, idx2char = load_vocab()
    lines = codecs.open(hp.test_data, 'r', 'utf-8').readlines()[1:]
    #print(lines)
    sents = [text_normalize(line.split(" ", 1)[-1]).strip() for line in lines] # text normalization, E: EOS
    lengths = [len(sent) for sent in sents]
    maxlen = sorted(lengths, reverse=True)[0]
    texts = np.zeros((len(sents), maxlen), np.int32)
    for i, sent in enumerate(sents):
        sum = ''
        texts[i, :len(sent)] = [char2idx[char] for char in sent]
        split_sents = sents[i].split(' ')
        l = len(split_sents)
        #print(sents[i].split(' '))
        for k in range(l):
            split_sents[k] = spell(split_sents[k])
            #print(split_sents[k])
            if(k==0):
                sum = split_sents[k]
            else:
                sum = sum + ' ' + split_sents[k]
        sents[i] = sum +'.E'
        #print(sents)


    return sents