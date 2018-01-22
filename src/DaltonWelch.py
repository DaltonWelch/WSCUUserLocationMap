# parse MS web services access log

import re
import datetime
import collections
import os
from os import listdir
from os.path import isfile, join
import matplotlib
import matplotlib.pyplot as plt


# match date/time, request type, requested uri, client ip
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

#one_dat = parse_file(os.path.join("weblogs","u_ex170601.log"))
#print(len(one_dat))
#print(len(set(l[3] for l in one_dat)))
#print(collections.Counter(datetime.datetime.strftime(l[0], "%y-%m-%d %H") for l in one_dat))
#dtex = one_dat[10][0]
#print(dtex.replace(minute=0, second=0))
#hrcounts = collections.Counter(l[0].replace(minute=0,second=0) for l in one_dat)
#hrcounts_sorted = sorted(hrcounts.items())
# matplotlib.rcParams['figure.figsize']=[15,10]
# plt.plot([e[1] for e in hrcounts_sorted])
# plt.savefig("hit.png")
# plt.show()

def parse_mult_files(ff):
    res = []
    for fname in ff:
        res += parse_file(os.path.join("weblogs", fname))
    return res

if __name__ == "__main__":

    file_list = ["u_ex170601.log", "u_ex170602.log", "u_ex170603.log", "u_ex170604.log", "u_ex170605.log", "u_ex170606.log", "u_ex170607.log"]
    one_week = parse_mult_files(file_list)

    print("Number of requests for whole week")
    print(len(one_week))
    print("Number of unique visitors")
    print(len(set(l[3] for l in one_week)))
    print("Number of requests per day")
    print(collections.Counter(datetime.datetime.strftime(l[0], "%y-%m-%d") for l in one_week))
    print("Number of requests for each hour of each day")
    print(len(collections.Counter(datetime.datetime.strftime(l[0], "%y-%m-%d %H") for l in one_week)))
    print((collections.Counter(datetime.datetime.strftime(l[0], "%y-%m-%d %H") for l in one_week)))
    print("Number of unique vistors for each hour of each day")

#print(onlyfiles[0])