fig = plt.figure(figsize = (12, 10))
ax = plt.axes(projection = '3d')

x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5, 5.1, 0.2)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

ax.set_xlabel('x', labelpad = 20)
ax.set_ylabel('y', labelpad = 20)
ax.set_zlabel('z', labelpad = 20)

fig.colorbar(surf, shrink = 0.5, aspect = 8)

plt.show()
