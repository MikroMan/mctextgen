import numpy as np
from random import randint
from random import random

SPECIAL = "!?."

def load_text(path):

    print('Loading text from file', path)
    text = []
    with open(path, "r", encoding="UTF-8") as in_file:
        for line in in_file:
            for word in line.split():
                buf = []
                while len(word) > 1 and word[-1] in SPECIAL:
                    buf.append(word[-1])
                    word = word[0:-1]
                text.append(word)
                for char in buf:
                    text.append(char)
    return text

def generate_matrix(text):
    uniques = list(set(text))
    uniques.sort()
    num_words = len(uniques)
    P = np.zeros(shape=(num_words,num_words))
    print('Processing data: {0} words, {1} unique... '.format(len(text), num_words), end='', flush=True)


    previous = text[0]
    for word in text[1:]:
        fst_idx= uniques.index(previous)
        snd_idx = uniques.index(word)

        previous = word
        P[fst_idx,snd_idx] += 1

    row_sums = P.sum(axis=1)
    for i in range(0,num_words):
        s = sum(P[i,])
        if s != 0.0:
            P[i,] /= sum(P[i,])


    print('Done')

    return {'words': uniques, 'trans_matrix': P}

def to_file(states, words, path):
    with open(path, "w", encoding='UTF-8') as out_file:
        buf = ""
        for state in states:
            if words[state] not in SPECIAL and len(buf) + len(words[state]) > 80 :
                out_file.write(buf.strip())
                out_file.write('\n')
                buf = words[state]
            else:
                if words[state] not in SPECIAL:
                    buf += ' '
                buf += words[state]

        if len(buf) > 0:
            out_file.write(buf)
            out_file.write('\n')



def generate_text(data, length=50):
    print('Generating {0} states... '.format(length), end='')
    P = data['trans_matrix']
    words = data['words']
    num_words = len(words)

    x0 = randint(0, num_words-1)

    while words[x0].islower():
        x0 = randint(0, num_words-1)

    states = [x0]

    c_sum = np.cumsum(P, axis=1)
    for i in range(0, length):
        rnd = random()
        row = c_sum[x0,]

        idx = np.where(row >= rnd)[0][0]
        states.append(idx)
        x0 = idx

    if '.' in words and words[states[-1]] not in SPECIAL:
        states.append(words.index('.'))

    print('Done')
    return states








