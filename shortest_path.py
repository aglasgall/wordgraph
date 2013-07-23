#!/usr/bin/python

import wordgraph
import sys

if len(sys.argv) < 4:
    print >>sys.stderr, "Usage: shortest_path.py <dictionary file> <word1> <word2>"
    sys.exit(1)

with open(sys.argv[1]) as f:
    wordlist = [line.strip() for line in f.readlines()]
    graph = wordgraph.graph(wordlist)
    path = graph.find_path(sys.argv[2], sys.argv[3])
    
    for word in path:
        print word

