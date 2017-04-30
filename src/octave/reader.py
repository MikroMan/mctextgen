#!/bin/python3
import sys
SPECIAL = ".!?"

previous = ''

def read(path):
    out = open("preprocess.txt", "w")
    print("Reading file from ", path);
    with open(path, "r") as file:
        for line in file:
            for word in line.split():

                buf = []
                while len(word) > 1  and word[-1] in SPECIAL:
                    buf.append(word[-1])
                    word = word[0:-1]
                out.write(word + " ")
                for char in buf:
                    out.write(char + " ")
    out.close()


if __name__ == "__main__":
    read(sys.argv[1])
