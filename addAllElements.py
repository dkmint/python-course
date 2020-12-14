x = np.array([[5, 6], [7, 8]])
n, m = x.shape
s = 0
for i in range(n):
    for j in range(m):
        s += x[i,j]
        
        
print(s)
