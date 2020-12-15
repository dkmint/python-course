def add_and_subtract(iterations):
    result = 1
    for i in range(iterations):
        result += 1/3
    for i in range(iterations):
        result -= 1/3
        
    return result

add_and_subtract(10000)
