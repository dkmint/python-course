def my_trig_sum(a, b):
    out1 = np.sin(a) + np.sin(b)
    out2 = np.sin(b) + np.cos(a)
    return out1, out2, [out1, out2]

a, b, e = my_trig_sum(2, 3)
print(f'a = {a}, b = {b}, e = {e}')
