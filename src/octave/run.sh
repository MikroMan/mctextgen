#!/bin/bash
OUT_FILE="./sample.out"
SRC_TXT="../data/butalci.txt"
WORD_LEN=100
python3 reader.py "$SRC_TXT"
echo "matrixgen(\"./preprocess.txt\", \".\"); quit;" | octave-cli
echo "Starting text generation"
echo "textgen(\".\", \"$OUT_FILE\", $WORD_LEN, -1); quit;" | octave-cli
rm preprocess.txt uniques matrixdump
python3 punctuation_clean.py "$OUT_FILE"
mv "$OUT_FILE.punct" "$OUT_FILE"
