import os
import pickle

USER = 'Tine Šubic'


def main():
    users = {}

    os.chdir('./dumps')
    path = os.getcwd() + '/'
    files = os.listdir('.')
    files.sort()

    for file in files:
        fp = path + file

        data = pickle.load(open(fp, 'rb'))
        for msg in data['msgs']:

            uname = msg['user'].replace('\n', ' ').strip()

            if uname not in users.keys():
                users[uname] = []
            lines = msg['text'].split('\n')
            for line in lines:
                users[uname].append(line.strip())
    i = 0
    for key in users.keys():
        i += len(users[key])
        print('{0} : {1}'.format(key, len(users[key])))

    os.chdir('..')
    with open('./chats/user.txt', 'w', encoding='UTF-8') as usertxt:
        for msg in users[USER]:
            usertxt.write(msg)
            usertxt.write('\n')

        usertxt.flush()

    with open('./chats/others.txt', 'w') as others:
        for key in users.keys():
            if USER not in key:
                for msg in users[key]:
                    others.write(msg)
                    others.write('\n')

    with open('./chats/all.txt', 'w') as all_msgs:
        for key in users.keys():
            for msg in users[key]:
                all_msgs.write(msg)
                all_msgs.write('\n')

if __name__ == '__main__':
    main()
