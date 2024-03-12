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



PubMed_Fields = [ "PMID", "OWN ", "STAT", "DCOM", "LR  ", "IS  ", "VI  ",
  "IP  ", "DP  ", "TI  ", "PG  ", "LID ", "AB  ", "CI  ", "FAU ", "AU  ",
  "AD  ", "LA  ", "GR  ", "PT  ", "DEP ", "PL  ", "TA  ", "JT  ", "JID ",
  "RN  ", "SB  ", "MH  ", "PMC ", "MID ", "OTO ", "OT  ", "COIS", "EDAT",
  "MHDA", "PMCR", "CRDT", "PHST", "AID ", "PST ", "SO  "]


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
