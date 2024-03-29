#! /usr/bin/python
'''Do some stats on authors of the selected publications.
Inputs: the appropriate search results saved in text PubMed format.
Stats: this version will output generic stats (# 1st, middle, last auth publications)
for the authors matching certain criteria.

NOTE: at the moment this is a generic stub. Will first finish the specific version,
then generalise later.
'''

#
# Copyright (C) 2018  George Shapovalov <gshapovalov@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#


import sys,argparse
from lib import refdata

def condition(text):
    "condition check, if True gets picked for processing"
    return "rance" in text # this is checking for France in passed text,


def ProcessCommandLine():
    parser = argparse.ArgumentParser(description='''do generic stats on authors of the search.

This calculates the generic stats on the authors of the saved search. The output stats are:
auth,  #1st, #middle, #last author publications, in tabular format that should be easy to import by any spreadhsheet software.
An optional cretirion can be entered/edited at the top to limit the stats on the authors only passing the check.
'''
)
    parser.add_argument('fn',  help="file names to process (expects text file in PubMed text format, *not* xml)")
#    parser.add_argument('dec', type=int, help="decimation factor (int)")
#    parser.add_argument('dir', choices=["pos","neg"], help="activity direction (one of pos or neg)")
#    parser.add_argument('-c', type=float, help="threshold crossing, above which  a max instead of regular is taken. Number between 0 and 1, 0.5 is the default (if omitted)")
    parser.add_argument('-o', help="name of output file. If omitted, replaces .ext with -stats.csv")
    parser.add_argument('-v', action='store_true', help="be verbose")
    return parser.parse_args()



# ------------------------------------------------
#main block
args = ProcessCommandLine()

# author stats will be kept in the dict of tuples, indexed by AU field -
# just a quick code/prototyping here. May make sense to encapsulate for more serious repeated use
# we will keep the AU as key, AD plus counts: first, mid, last in a tuple as dict value

auStats = {}


with open(args.fn) as F:
    data = refdata.RefAuthors()
    while data.readRefBlock(F):
        data.print()
        for i in range(len(data.authors)):
            FAU,AU,AD = data.authors[i]
            if condition(AD):
                # increment appropriate counters, create new dict entry if new author
                if AU in auStats:
                    #unpack the tuple first
                    aAD, aFirst, aMid, aLast = auStats[AU]
                    if i == 0:
                        # 1st author
                        aFirst += 1
                    elif i == len(data.authors):
                        # last author
                        aLast  += 1
                    else:
                        aMid   += 1
                    auStats[AU] = aAD, aFirst, aMid, aLast
                else: # AU not in auStats
                    # create new entry
                    aFirst, aMid, aLast = 0, 0, 0
                    if i == 0: # NOTE: repetition! should encap this if block in function
                        # 1st author
                        aFirst += 1
                    elif i == len(data.authors):
                        # last author
                        aLast  += 1
                    else:
                        aMid   += 1
                    auStats[AU] = (AD, aFirst, aMid, aLast)

