#!/usr/bin/env python

from poe.item import from_description

def get_ref(which):
    with open("references/%s" % which) as f:
        return "".join(f.readlines())


map_file = get_ref("map")
incubator_file = get_ref("incubator")

map = from_description(map_file)
print(map)

incubator = from_description(incubator_file)
print(incubator)