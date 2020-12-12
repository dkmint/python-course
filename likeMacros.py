def my_fun_plus_one(f, x):
    return f(x) + 1

print(my_fun_plus_one(np.sin, np.pi/2))
print(my_fun_plus_one(np.cos, np.pi/2))
print(my_fun_plus_one(np.sqrt, 25))

print(my_fun_plus_one(lambda x: x + 2, 2))
