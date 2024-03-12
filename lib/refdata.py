#
# Principal data structs encapsulating reference data
# Copyright (C) 2018  George Shapovalov <gshapovalov@gmail.com>
#
# This is the principal part of the underlying library that handles reference structure
# and the corresponding collections.
#
# This version utilises in-build lists and dicts. This should work Ok for the medium
# reference colections (1000s to 100k or so, maybe up to 1M), but will likely lead
# to memory overflows and glacial processing speed for anything larger. But this is
# easy starting implementation, which should be sufficient for most situations.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

from .refdata_common import *

class RefAuthors:
    """Just the author info of the reference.
    Stores only PMID, authors and affiliations.
    """

    def __init__(self):
        "Setup minimalistic params that should be always there"
        self.PMID = 0
        self.authors = []

    def readRefBlock(self, F):
        "read reference entry in PubMed text format from open file F"
        # NOTE!!!
        # This expects the F to be open and positioned at the 1st line of ref block !!!
        # i.e., at the beginning (1srt line) of file, or right after the empty line ending next block
        #
        # PubMed text format is strictly ordered, so just go along with the logic
        line = F.readline()
        if PMF_header(line) != PMF_PMID:
            raise Format_Error
        self.PMID = int(PMF_value(line))
        #
        #now skip until the 1st FAU field encountered
        while PMF_header(line) != PMF_FAU:
            line = F.readline()
        #
        # now we are on the 1st line of 1st author, cycle through all authors
        while PMF_header(line) == PMF_FAU:
            # store the FAU value
            authFAU = PMF_value(line)
            #
            # now process the AU part
            line = F.readline()
            if PMF_header(line) != PMF_AU:
                raise Format_Error
            authAU = PMF_value(line)
            #
            # now process the AD part
            line = F.readline()
            if PMF_header(line) != PMF_AD:
                raise Format_Error
            authAD = [PMF_value(line)] # can be multiline
            line = F.readline()
            while PMF_header(line) == PMF_EMPTY:
                authAD.append(PMF_value(line))
                line = F.readline()
            self.authors.append((authFAU,authAU,authAD))
        #
        # end of authors parse
        # now read until the end of the ref block, to reset position properly for next rader
        while line != "":
            line = F.readline()
            #print(line)
        #print(self.PMID, self.authors)


    def print(self):
        "print ref auntor info to stdout. Primarily for testing"
        print("PMID:", self.PMID)
        for auth in self.authors:
            FAU, AU, AD = auth
            print("FAU :", FAU)
            print("AU  :", AU)
            print("AD  :", AD[0])
            for line in AD[1:]:
                print("     ", line)
        print()


# NOTE! refactor: derive from Auths or make a casacde of details
class RefData:
    """Reference encapsulation class.
    This follows the PubMed fields as given in text format.
    Complete and compact versions to be provided.
    """

    def __init__(self):
        "Setup minimalistic params that should be always there"
        self.PMID = 0
        self.authors = []

    def fromTxt(self, F):
        "read reference entry in PubMed text format from open file F"
        for line in F:
            if line == "": break #end of ref block

