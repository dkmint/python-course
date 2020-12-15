x = np.arange(11)
y = x**2

plt.figure(figsize = (14, 8))

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title('Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title('Scatter')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 3)
plt.bar(x, y)
plt.title('Bar')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 4)
plt.loglog(x, y)
plt.title('Loglog')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which = 'both')

plt.subplot(2, 3, 5)
plt.semilogx(x, y)
plt.title('Semilogx')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which = 'both')

plt.subplot(2, 3, 6)
plt.semilogy(x, y)
plt.title('Semilogy')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.tight_layout()

plt.show()
