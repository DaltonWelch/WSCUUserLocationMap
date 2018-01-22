import re
import collections
import datetime

with open("weblogs/u_ex170601.log") as f:
    lines = f.readlines()
#datetime, cs method, uri, c-ip, reger, status
regex = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) [\w\d.]+\s([A-Z]+)'
extractor = re.compile(regex)
print(extractor.match(lines[5]).groups())


#def parse_dt(dtstr):
    #return datetime.datetime.strptime(dtstr, "%d/%b/%Y:%H:%M:%S %z")



print(lines[5])
