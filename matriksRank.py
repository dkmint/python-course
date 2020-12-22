from numpy.linalg import cond, matrix_rank
A = np.array([[1,1,0],
             [0,1,0],
             [1,0,1]])
print('Condition number:\n', cond(A))
print('Rank:\n', matrix_rank(A))
y = np.array([[1], [2], [1]])
A_y = np.concatenate((A, y), axis = 1)
print('Augmented matrix:\n', A_y)
