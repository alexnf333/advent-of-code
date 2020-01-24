import time
import re
from statistics import mode
from collections import Counter

register = []
info = [[],[],[]]
tic=time.time()
with open("inputs04.txt", "r") as ins:
    for line in ins:
        register.append(line)
ins.close()
register.sort()
len_reg = len(register)
for i in range(len_reg):
    found = re.search('#(.+?) begins', register[i])
    if found:
        id = found.group(1)
        if id not in info[0]:
            info[0].append(id)
            info[1].append([])
            info[2].append(0)
        j = info[0].index(id)
    else:
        if register[i].find('falls') != -1:
            found = re.search(':(.+?)]', register[i])
            min_start = int(found.group(1))
        else:
            if register[i].find('wakes') != -1:
                found = re.search(':(.+?)]', register[i])
                min_end = int(found.group(1))
                info[1][j] += list(range(min_start, min_end))
                info[2][j] += min_end-min_start

most_time = max(info[2])
index_most_time = info[2].index(most_time)
min_most_rep = mode(info[1][index_most_time])

sleepy = [[],[]]
len_info = len(info[1])
for i in range(len_info):
    a = Counter(info[1][i]).most_common(1)

    try:
        sleepy[0].append(a[0][0])
        sleepy[1].append(a[0][1])
    except:
        sleepy[0].append(0)
        sleepy[1].append(0)

most_rep = max(sleepy[1])
index_most_rep = sleepy[1].index(most_rep)
min_rep_all = sleepy[0][index_most_rep]

print("result 1: ", int(info[0][index_most_time])*min_most_rep)
print("result 2: ", int(info[0][index_most_rep])*min_rep_all)
print('time: {} secs'.format(time.time()-tic))
