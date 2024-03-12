# Copyright (C) 2024  George Shapovalov <gshapovalov@gmail.com>
#
# Common data structures, exceptions, etc.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#


class RefData_Error(Exception):
    """Base module exception."""
    pass

class Format_Error(RefData_Error):
    "base IO formatting exception, can be subclassed"

class RefData_EOF(RefData_Error):
    "EOF while parsing ref blocks - may be used for flow coltrol"


### --------- ###
# helper function, use these instead of direct spec in-code, even if small!

# PubMed text format is positional, the format spec is the 1st 4 chars
# then the '- ' separator (unless fleid continuation, then its '  ')
# then the readable field value

def PMF_header(line):
    "returns the header part of the line"
    return line[:4]

def PMF_value(line):
    "returns value part of the field"
    # it lways starts at char 7, even with field continuation
    return line[6:].strip()



PubMed_Fields = [ "    ",
  "PMID", "OWN ", "STAT", "DCOM", "LR  ", "IS  ", "VI  ", "IP  ", "DP  ", "TI  ",
  "PG  ", "LID ", "AB  ", "CI  ", "FAU ", "AU  ", "AD  ", "LA  ", "GR  ", "PT  ",
  "DEP ", "PL  ", "TA  ", "JT  ", "JID ", "RN  ", "SB  ", "MH  ", "PMC ", "MID ",
  "OTO ", "OT  ", "COIS", "EDAT", "MHDA", "PMCR", "CRDT", "PHST", "AID ", "PST ",
  "SO  "]

# "    " - continuation of previous field, implicit, starting at 0
# PMID - 1
# FAU - 15, AU - 16, AD - 17


PMFidx_EMPTY  = 0
PMFidx_PMID   = 1
PMFidx_FAU    = 15
PMFidx_AU     = 16
PMFidx_AD     = 17

PMF_EMPTY = PubMed_Fields[PMFidx_EMPTY]
PMF_PMID  = PubMed_Fields[PMFidx_PMID]
PMF_FAU   = PubMed_Fields[PMFidx_FAU]
PMF_AU    = PubMed_Fields[PMFidx_AU]
PMF_AD    = PubMed_Fields[PMFidx_AD]



PubMed_FieldDict = {
   "PMID":"PMID article ID",
   "OWN ":"db name, major?",
   "STAT":"db name, minor?",
   "DCOM":"date, submission?",
   "LR  ":"",
   "IS  ":"",
   "VI  ":"",
   "IP  ":"",
   "DP  ":"",
   "TI  ":"",
   "PG  ":"",
   "LID ":"",
   "AB  ":"",
   "CI  ":"",
   "FAU ":"author name, full",
   "AU  ":"author name, short",
   "AD  ":"author affiliation (author data?)",
   "LA  ":"",
   "GR  ":"",
   "PT  ":"",
   "DEP ":"",
   "PL  ":"",
   "TA  ":"",
   "JT  ":"",
   "JID ":"",
   "RN  ":"",
   "SB  ":"",
   "MH  ":"",
   "PMC ":"",
   "MID ":"",
   "OTO ":"",
   "OT  ":"key words?",
   "COIS":"disclosures",
   "EDAT":"",
   "MHDA":"",
   "PMCR":"",
   "CRDT":"",
   "PHST":"",
   "AID ":"",
   "PST ":"",
   "SO  ":"" }
