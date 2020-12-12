a = ['One', 'Two', 'Three']
b = [1, 2, 3]

z = zip(a, b)
y = list(z)
print(y)
c, d = zip(*y)
print(c, d)
for i, j in zip(a, b):
    print (i, j)
