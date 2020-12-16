# from mpl_toolkits import mplot3d
# plt.style.use('seaborn-poster')

x = np.random.random(50)
y = np.random.random(50)
z = np.random.random(50)

fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection = '3d')
ax.grid()

ax.scatter(x, y, z, c = 'r', s = 50)
ax.set_title('3D Scatter Plot')

ax.set_xlabel('x', labelpad = 20)
ax.set_ylabel('y', labelpad = 20)
ax.set_zlabel('t', labelpad = 20)

plt.show()
