def from_description(desc):
    """
    returns an Item (or subclass) from a copy/pasted description 
    of an item
    """
    raw = desc.split("\n")
    for line in raw:
        if "Item Class" in line:
            item_class = get_property(line)
    

    if item_class == "Maps":
        return createMap(desc)
    elif item_class == "Incubators":
        return createIncubator(desc)

    else:
        return None


def from_json(json):
    """
        returns an Item (or subclass) from a json input
    """
    pass


def get_property(line):
    if ":" not in line: return line.lstrip().rstrip()
    try:
        x, line = line.split(": ")
        return line.rstrip().lstrip()
    except:
        print(line)
        raise Exception("received invalid line")

def parse_metadata(item_metadata):
    try:
        item_class, rarity, name, x = item_metadata.split("\n")
    except:
        print(item_metadata)
        print(item_metadata.split("\n"))
        raise Exception("more than 3 lines probably a different item type")


    item_class = get_property(item_class)
    rarity = get_property(rarity)
    name = get_property(name)

    return item_class, rarity, name

def createMap(data):
    m = Map()

    item_metadata, tier, ilvl, descr = data.split("--------")
    m.item_class, m.rarity, m.name = parse_metadata(item_metadata)
    m.tier = get_property(tier)
    m.item_level = get_property(ilvl)
    m.description = descr

    return m

def createIncubator(data):
    i = Incubator()
    item_metadata, stack_size, ilvl, x, y = data.split("--------")
    i.item_class, i.rarity, i.name = parse_metadata(item_metadata)
    i.stack_size = get_property(stack_size)
    i.item_level = get_property(ilvl)
    return i




class Item:
    """
    can consider adding things like icon and the rest if needed as part of a 
    load() method
    """

    def __init__(self):
        self.rarity = None
        self.name = None
        self.item_class = None
        self.item_level = None
        self.description = None

    def to_json(self):
        pass
    
    def __repr__(self):
        return self.name

class Incubator(Item):
    """
        make stackable class?
    """
    def __init__(self):
        self.stack_size = None
        super().__init__()


class Map(Item):
    def __init__(self):
        super().__init__()
        self.tier = None
    
    def __repr__(self):
        return "%s\n%s" % (self.name, self.tier)
