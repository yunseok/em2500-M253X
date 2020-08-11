import json
import timeago as timesince

from collections import namedtuple

def get(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("ARG UNKNOWN!!!")
    except FileNotFoundError:
        raise FileNotFoundError("JSON FILE NOT FOUND!!")

def timeago(target):
    return timesince.format(target)