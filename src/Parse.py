import re
import datetime
import collections
import os
from os import listdir
from os.path import isfile, join
import matplotlib
import matplotlib.pyplot as plt

regex = r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+[\d\w.]+\s([A-Z]+)\s+([^\s]+)\s+\S+\s+\d+\s+\S+\s([\d\w.]+)"
extractor = re.compile(regex)

def parse_line(line):
    """
    Parse a single line using the extractor
    """
    pieces = extractor.match(line).groups()
    dt=datetime.datetime.strptime(pieces[0],"%Y-%m-%d %H:%M:%S")
    # make a tuple with dt and the rest (splatted)
    return (dt, *pieces[1:])

def parse_file(log_path):
    with open(log_path) as f:
        lines = f.readlines()
    lines = [l for l in lines if l[0]!="#"]
    return [parse_line(l) for l in lines]

print(parse_file("WebLogs/TestLog.log"))