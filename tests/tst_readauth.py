#! /bin/env python
# Testing single reference parse, author info only
# Copyright (C) 2018  George Shapovalov <gshapovalov@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

import sys

#sys.path.append("..")
from lib import refdata


fn  = "../dat/test_ref.txt"
fns = "../dat/test_refs.txt"

print("testing parse of a single reference; author info")

data = refdata.RefAuthors()
with open(fn) as F:
    data.readRefBlock(F)
    data.print()

print()
print("testing parse of multiple ref blocks; author info")

with open(fns) as F:
    data = refdata.RefAuthors()
    while data.readRefBlock(F):
        data.print()
