import numpy as np

def my_newton(f, df, x0, tol):
    if abs(f(x0)) < tol:
        return x0
    else:
        return my_newton(f, df, x0 - f(x0)/df(x0), tol)
    

f = lambda x: x**2 - 2
f_prime = lambda x: 2 * x
newton_raphson = 1.4 -(f(1.4) / f_prime(1.4))
estimate = my_newton(f, f_prime, 1.5, 1e-6)

print('newton_raphson = ', newton_raphson)
print('estimate = ', estimate)
print('sqrt(2) = ', np.sqrt(2))
