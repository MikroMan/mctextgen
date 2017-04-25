from bs4 import BeautifulSoup
from prompt_toolkit.terminal.vt100_input import _Flush
from time import time


def parse(path):
    fid = open(path)
    print("Loading html from ", path, '...', end='', flush=True)
    start = time()
    soup = BeautifulSoup(fid, 'html.parser')
    print("Done: ", time() - start)

#Try bypassing contents directly to thread - eliminate a giant search

    threads = soup.find_all('div', class_='thread')

    chats = {}

    print('Found', len(threads), ' threads', flush=True)
    for thread in threads:
        identifier = thread.contents[0].strip().replace('@facebook.com', '')
        chats[identifier] = {'num_id': identifier, 'msg_count':0, 'msgs': []}

        messages = thread.find_all('div', class_='message')
        divs = thread.find_all('p')

        for i in range(0, len(messages)):
            metadata = messages[i]
            txt = divs[i]
            msg = {'user': metadata.find_all('span', class_='user')[0].contents, 'txt': txt.text.strip().replace('\n', ' ')}
            chats[identifier]['msgs'].append(msg)
            chats[identifier]['msg_count'] += 1



        print('done')














if __name__ == '__main__':
    path = "./dump/html/messages.htm"
    parse(path)