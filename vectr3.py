from numpy import arccos, dot

v = np.array([[10, 9, 3]])
w = np.array([[2, 5, 12]])
theta = arccos(dot(v, w.T) / (norm(v) * norm(w)))
print(theta)
