def my_dist_xyz(x, y, z):
    """x, y, z are 2D coordinates contained in a tuple
    output:
    d - list, where
    d[0] is the distance between x and y
    d[1] is the distance between x and z
    d[2] is the distance between y and z"""
    def my_dist(x, y):
        """subfunction for my_dist_xyz
        Output is the distance between x and y,
        computed using the distance formula"""
        out = np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        return out
    
    d0 = my_dist(x, y)
    d1 = my_dist(x, z)
    d2 = my_dist(y, z)
    
    return [d0, d1, d2]

d = my_dist_xyz((0, 0), (0, 1), (1, 1))
print(d)
