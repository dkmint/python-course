def my_adder(a, b, c):
    # Check for erronius input
    if not (isinstance(a, (int, float)) \
           or isinstance(b, (int, float)) \
            or isinstance(c, (int, float))):
        raise TypeError('Inputs must be numbers.')
        
    return a + b + c
    
    
x = my_adder(1.1, 2.2, 3.3)
print(x)
