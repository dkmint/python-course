with open('auto-mpg.data') as f:
    for line_index, line in enumerate(f):
        print(line)
        if line_index == 5:
            break
