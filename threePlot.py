from mpl_toolkits import mplot3d
plt.style.use('seaborn-poster')

fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection = '3d')
ax.grid()
t = np.arange(0, 10*np.pi, np.pi/50)
x = np.sin(t)
y = np.cos(t)
ax.plot3D(x, y, t)
ax.set_title('3D Parametric Plot')

ax.set_xlabel('x', labelpad = 20)
ax.set_ylabel('y', labelpad = 20)
ax.set_zlabel('t', labelpad = 20)

plt.show()
