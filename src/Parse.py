import re
import datetime
import win_inet_pton
from geoip import geolite2


regex = r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+[\d\w.]+\s+[A-Z]+\s+[^\s]+\s+\S+\s+\d+\s+\S+\s([\d\w.]+)"
extractor = re.compile(regex)

def parse_line(line):
    """
    Parse a single line using the extractor
    """
    pieces = extractor.match(line).groups()
    dt=datetime.datetime.strptime(pieces[0],"%Y-%m-%d %H:%M:%S")
    # make a tuple with dt and the rest (splatted)
    return (dt, pieces[1])

def parse_file(log_path):
    """
    ignores unimportant log text and runs parse_line on the rest
    to return list of parsed lines.
    """
    with open(log_path) as f:
        lines = f.readlines()
    lines = [l for l in lines if l[0]!="#"]
    return [parse_line(l) for l in lines]

def lookup_address(ip):
    """
    takes in ip address and returns geoip lookup location data as a string.
    """
    match = geolite2.lookup(ip)
    if (match is None):
        return 0, 0
    else:
        return match.location

if __name__ == "__main__":
    """
    test
    """

    parseTest = parse_file("WebLogs/TestLog.log")
    #print(parseTest)
    unique_visitors = set(x[1] for x in parseTest)
    for v in unique_visitors:
        ip = v
        final_list = (ip, lookup_address(ip))

    print(final_list)

