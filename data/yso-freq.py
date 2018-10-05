#!/usr/bin/env python3

import sys
import os.path

subjdir = sys.argv[1]

def file_lines(fn):
    with open(fn) as f:
        return len(f.readlines())

def freq(uri):
    ln = uri[1:-1].split('/')[-1]
    return file_lines(os.path.join(subjdir, ln + "-fi.txt")) - 2

for line in sys.stdin:
    uri, label = line.strip().split("\t", 1)
    print("\t".join((uri, str(freq(uri)), label)))
