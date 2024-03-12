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

import sys

class RefAuthors:
    """Just the author info of the reference.
    Stores only PMID, authors and affiliations.
    """

    def __init__(self):
        "Setup minimalistic params that should be always there"
        self.PMID = 0
        self.authors = []

    def fromTxt(self, F)
        "read reference entry in PubMed text format from open file F"
        # PubMed text format is strictly ordered, so just go along with the logic
        line = F.readline()
        if
        for line in F:
            if line == "": break #end of ref block



class RefData:
    """Reference encapsulation class.
    This follows the PubMed fields as given in text format.
    Complete and compact versions to be provided.
    """

    def __init__(self):
        "Setup minimalistic params that should be always there"
        self.PMID = 0
        self.authors = []

    def fromTxt(self, F)
        "read reference entry in PubMed text format from open file F"
        for line in F:
            if line == "": break #end of ref block

