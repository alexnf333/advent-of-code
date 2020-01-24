import time
freq = 0
twice = 0
history = []
lap = 0
tic=time.time()
while twice == 0:
    with open("inputs01.txt", "r") as ins:
        for line in ins:
            if line != '\n':
                freq += int(line)
                if twice == 0:
                    if freq not in history:
                        history.append(freq)
                    else:
                        twice = 1
                        twice_freq = freq
    if lap == 0:
        result_freq = freq
        lap = 1
ins.close()
print("resulting frequency: ", result_freq)
print("reached twice: ", twice_freq)
print('time: {} secs'.format(time.time()-tic))
