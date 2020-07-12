i = 0
while i<100:
    i = i + 1
    if i%7 == 0:
        continue
    elif str(i).find("7") != -1:
        continue
    else:
        print(i)
