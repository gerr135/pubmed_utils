#! /bin/env python
# Testing single reference import, full version
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

print("testing parse of a single reference")

sys.exit("not implemented yet")
data = refdata.RefData()
with open(fn) as F:
    data.read_csv(F, Separator)
    data.write_csv(sys.stdout, Separator)

