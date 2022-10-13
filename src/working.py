#!/usr/bin/env python

from poe.item import from_description


with open("references/map") as f:
    whole_file = "".join(f.readlines())


x = from_description(whole_file)
print(x)