try:
    f = open("/home/dmint/Desktop/pr_02_1.in", 'r')
    # print(*f)
    # while True:
    lineCount = 0
    for line in f:
        sline = line.split()
        lineCount = lineCount + 1
        # print(len(sline))
        if len(sline) < 2:
            print("Error! Not enough data at line ", lineCount)
            break

        elif len(sline) > 2 and sline[0] != 'initUcell':
            print("Error! Too many data! ", lineCount)
            break
        elif sline[0] == 'initUcell' and len(sline) > 4:
            print("Error! Too many data! ", lineCount)
            break
        elif sline[0] == 'initUcell' and len(sline) < 3:
            print("Error! Not enough data at line ", lineCount)
            break
        elif sline[0] == 'initUcell' and len(sline) == 3:
            description = sline[0]
            x = sline[1]
            y = sline[2]
            print(description, x, y)
            continue
        elif sline[0] == 'initUcell':
            description = sline[0]
            x = sline[1]
            y = sline[2]
            z = sline[3]
            print(description, x, y, z)
            continue
        description = sline[0]
        value = sline[1]
        print(description, value)

except IOError:
    print("An IOError has occured!")
finally:
    f.close()
