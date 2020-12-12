def circle_calc(calc, r):
    if calc == 'area':
        return np.pi * r**2
    elif calc == 'circumference':
        return 2 * np.pi * r
    
area = circle_calc('area', 2.5)

circumference = circle_calc('circumference', 2.5)
print(area, circumference)

circle_calc('area', np.array([2, 3, 4]))
