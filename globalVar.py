n = 42

def func():
    global n
    print(f'Within function: n is {n}')
    n = 3
    print(f'Within function: n changed to {n}')
    
func()
print(f'Outside function: n is {n}')
