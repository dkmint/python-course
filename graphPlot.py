x = [0, 1, 2, 3]
y = [0, 1, 4, 9]
plt.plot(x, y)
plt.show()

x = np.linspace(-5, 5, 100)
plt.plot(x, x**2)
plt.show()

%matplotlib inline
x = np.linspace(-5,5, 100)
plt.plot(x, x**2, "g-")
plt.show()

x = np.linspace(-5,5,20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")
plt.show()

plt.figure(figsize= (10,  6))
x = np.linspace(-5,5,20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")
plt.title(f"Plot of Various Polynomials from {x[0]} to {x[-1]}")
plt.xlabel("X axis", fontsize=18)
plt.ylabel("Y axis", fontsize=18)
plt.show()

plt.style.use("seaborn-poster")
plt.figure(figsize= (10,  6))
x = np.linspace(-5,5,20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")
plt.title(f"Plot of Various Polynomials from{x[0]}to{x[-1]}")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

plt.figure(figsize= (10,  6))
x = np.linspace(-5,5,20)
plt.plot(x, x**2, "ko", label= "quadratic")
plt.plot(x, x**3, "r*", label= "cubic")
plt.title(f"Plot of Various Polynomials from{x[0]}to{x[-1]}")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc=2)
plt.show()

plt.figure(figsize = (10, 6))

x = np.linspace(-5, 5, 100)

plt.plot(x, x**2, 'ko', label = 'quadratic')
plt.plot(x, x**3, 'r*', label = 'cubic')
plt.title(f'Plot of Various Plolynomials from {x[0]} to {x[-1]}')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend(loc = 2)
plt.xlim(-6, 6)
plt.ylim(-10, 10)
plt.grid()
plt.show()


