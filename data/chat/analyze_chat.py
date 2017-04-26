from bs4 import BeautifulSoup
import lxml
import pickle
from time import time
import sys

def parse(path):
    fid = open(path)
    print("Loading html from ", path, '...', end='', flush=True)
    start = time()
    soup = BeautifulSoup(fid, 'lxml')
    print("Done: ", time() - start)

#Try bypassing contents directly to thread - eliminate a giant search

    soup = soup.find_all('div', class_='thread')

    chats = {}

    print('Found', len(soup), ' threads', flush=True)
    i = 1

    for thread in soup:
        identifier = thread.contents[0].strip().replace('@facebook.com', '')
        chats[identifier] = {'num_id': identifier, 'msg_count':0, 'msgs': []}


        children = thread.findChildren()

        msg = {}
        for child in children:
            if child.has_attr('class') and child.get('class')[0] == 'user':
                msg['user'] = child.text
            elif (not child.has_attr('class')) and child.name == 'p':
                msg['text'] = child.text
                chats[identifier]['msgs'].append(msg)
                chats[identifier]['msg_count'] += 1
                #print(msg['user'], ':', msg['text'], flush=True)
                msg = {}


        pickle.dump(chats[identifier], open("./dumps/" + str(i)+ ".dump", 'wb' ))
        i+=1

    pickle.dump(chats, open('./full_dump.dump', 'wb'))














if __name__ == '__main__':
    path = "./dump/html/messages.htm"
    parse(path)