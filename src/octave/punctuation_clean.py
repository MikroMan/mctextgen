#!/bin/python3
import sys
SPECIAL = ".!?"


def read(path):
    out = open(path + ".punct", "w")
    print("Reading file from ", path);
    with open(path, "r") as file:
        for line in file:
            for word in line.split():
                if word not in SPECIAL:
                    out.write(" ")
                
                out.write(word)
    out.close()


if __name__ == "__main__":
    read(sys.argv[1])
