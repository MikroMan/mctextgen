import numpy as np
from random import randint
from random import random
from progress.bar import Bar

SPECIAL = "!?."


def load_text(path):
    print('Loading text from file', path)
    text = []
    with open(path, "r", encoding="UTF-8") as in_file:
        for line in Bar('Loading txt:').iter(in_file):
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
    P = np.zeros(shape=(num_words, num_words))
    print('Processing data: {0} words, {1} unique... '.format(len(text), num_words), flush=True)

    previous = text[0]
    bar = Bar('Generating matrix:', max=len(text) + num_words * 2)

    wds = {}
    for word in uniques:
        wds[word] = uniques.index(word)
        bar.next()

    for word in text[1:]:
        P[wds[previous], wds[word]] += 1
        previous = word
        bar.next()

    for i in range(0, num_words):
        s = sum(P[i,])
        if s != 0.0:
            P[i,] /= sum(P[i,])
        bar.next()
    bar.finish()

    return {'words': uniques, 'trans_matrix': P}


def to_file(states, words, path):
    with open(path, "w", encoding='UTF-8') as out_file:
        buf = ""
        for state in states:
            if words[state] not in SPECIAL and len(buf) + len(words[state]) > 80:
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
    words = data['words']
    num_words = len(words)

    x0 = randint(0, num_words - 1)

    while words[x0].islower():
        x0 = randint(0, num_words - 1)

    return get_states(x0, data, length, words)

def gen_seeded(data, length, x0):
    return get_states(x0, data, length, data['words'])

def get_states(x0, data, length, words):
    states = [x0]
    if 'sum' not in data:
        data['sum'] = np.cumsum(data['trans_matrix'], axis=1)
    bar = Bar('Generating states:', max=length)
    for i in range(0, length):
        idx = np.where(data['sum'][x0,] >= random())[0][0]
        states.append(idx)
        x0 = idx
        bar.next()

    bar.finish()

    if '.' in words and words[states[-1]] not in SPECIAL:
        states.append(words.index('.'))
    return states
