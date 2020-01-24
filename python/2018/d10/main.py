
import time
import re
import copy

info = [[],[],[],[]]
tic=time.time()
with open("inputs10.txt", "r") as ins:
    for line in ins:
        foundx = re.search('n=<(.+?), ', line)
        foundy = re.search(', (.+?)> v', line)
        foundvx = re.search('y=<(.+?), ', line)
        foundvy = re.search('>(.+?) ,', line[::-1])
        x = int(foundx.group(1))
        y = int(foundy.group(1))
        vx = int(foundvx.group(1))
        vy = int(foundvy.group(1)[::-1])
        info[0].append(x)
        info[1].append(y)
        info[2].append(vx)
        info[3].append(vy)
ins.close()

len_info = len(info[0])
info2 = copy.deepcopy(info)
global_min = max(info2[0])-min(info2[0])
global_min2 = max(info2[1])-min(info2[1])
for i in range(50000):
    for j in range(len_info):
        info2[0][j] += info2[2][j]
        info2[1][j] += info2[3][j]
    if max(info2[0])-min(info2[0]) < global_min:
        maxim = max(info2[0])
        minim = min(info2[0])
        global_min = maxim - minim
        index = i
    if max(info2[1])-min(info2[1]) < global_min2:
        maxim2 = max(info2[1])
        minim2 = min(info2[1])
        global_min2 = maxim2 - minim2
        index2 = i

list = []
for i in range(index+1):
    for j in range(len_info):
        info[0][j] += info[2][j]
        info[1][j] += info[3][j]
for i in range(len_info):
    list.append((info[1][i],info[0][i]))

for i in range(minim2, maxim2+1):
    for j in range(minim, maxim+1):
        if (i,j) in list:
            print("#", end="")
        else:
            print(".", end="")
    print(".\n", end="")

print("seconds they would have needed to wait: ", index+1)
print('time: {} secs'.format(time.time()-tic))
