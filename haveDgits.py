def have_digits(s):
    out = 0
    for c in s:
        if c.isdigit():
            out = 1
            break
            
    return out

out1 = have_digits('only4you')
out2 = have_digits('only for you')
print(out1, out2)
