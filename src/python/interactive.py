import pickle

import markov
import os

session_data = {}
old_gen = []
old_command = ['show']


def load_data(commands):
    if commands[1] == 'raw':
        if 'txt' not in session_data:
            print('No text loaded, run \'read <file>\'')
            return
        session_data['markov_data'] = markov.generate_matrix(session_data['txt'])
    elif commands[1] == 'dump':
        if len(commands) < 3:
            print('No filename argument provided')
            return
        session_data['markov_data'] = pickle.load(open(commands[2], 'rb'))
        print('Loaded file: {0} unique words.'.format(len(session_data['markov_data']['words'])))


def print_stdout(states):
    buf = ""
    words = session_data['markov_data']['words']
    for state in states:
        if words[state] not in markov.SPECIAL and len(buf) + len(words[state]) > 80:
            print(buf.strip())
            buf = words[state]
        else:
            if words[state] not in markov.SPECIAL:
                buf += ' '
            buf += words[state]

    if len(buf) > 0:
        print(buf)


def generate(commands):
    global old_gen
    length = commands[1]
    if 'markov_data' not in session_data:
        print('Missing Markov Chain data.')
        return

    states = markov.generate_text(session_data['markov_data'], int(length))
    old_gen = states
    if commands[2] == '-':
        print_stdout(states)
    else:
        markov.to_file(states, session_data['markov_data']['words'], commands[2])


def print_stats():
    if 'markov_data' in session_data:
        print('Markov Chain data loaded: YES')
        print('Loaded file: {0} unique words.'.format(len(session_data['markov_data']['words'])))
    else:
        print('Markov Chain data loaded: NO')
        if 'txt' in session_data:
            print('Text loaded: YES. Length:', len(session_data['txt']))
        else:
            print('Text loaded: NO (run \'load dump <file>\' or \'read <file>\')')


def parse_input(commands):
    global session_data
    global old_command

    if len(commands) < 1:
        print('Invalid command.')
        return True
    elif commands[0] == 'read':
        session_data['txt'] = markov.load_text(commands[1])
    elif commands[0] == 'load':
        load_data(commands)
    elif commands[0] == 'gen':
        generate(commands)
    elif commands[0] == 'dump':
        pickle.dump(session_data['markov_data'], open(commands[1], 'wb'), protocol=4)
    elif commands[0] == 'cd':
        os.chdir(commands[1])
    elif commands[0] == 'pwd':
        print(os.getcwd())
    elif commands[0] == 'exit':
        return True
    elif commands[0] == 'ls':
        print(os.listdir('.'))
    elif commands[0] == 'rm':
        os.remove(commands[1])
    elif commands[0] == 'clean':
        session_data = {}
    elif commands[0] == 'show':
        print_stats()
    elif commands[0] == 'save':
        if len(commands) < 2:
            print('No filename argument provided')
        else:
            if len(old_gen) > 0:
                markov.to_file(old_gen, session_data['markov_data']['words'], commands[1])
    elif commands[0] == '!!':
        b = parse_input(old_command + commands[1:])
        if len(commands) > 1:
            old_command = old_command + commands[1:]
        return b

    old_command = commands
    return False


def interactive_session():
    end = False
    while not end:
        stdin = input('[msh]>')

        end = parse_input(stdin.split(' '))
