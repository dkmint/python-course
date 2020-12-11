square = lambda x: x**2
print(square(2))
print(square(5))

my_adder = lambda x, y: x + y
print(f'my_adder is {my_adder(2, 5)}')

sorted([(1,2), (2,0), (4,1)], key = lambda x: x[1])
