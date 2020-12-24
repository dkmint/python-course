def f(x, y):
    return -2.0 * y * x


x = float(input('Initial condition x(0) = '))
y = float(input('Initial condition y(0) = '))
dx = float(input('Step size dx = '))
n = int(input('Number of iteration to be computed = '))
for i in range(n):
    x1 = x + dx
    y1 = y + dx * f(x, y)
    print(i, x1, y1)
    x = x1
    y = y1
