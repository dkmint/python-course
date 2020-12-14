def dist_2_points(xy_points, xy):
    d = []
    for xy_point in xy_points:
        dist = np.sqrt((xy_point[0] - xy[0])**2 + (xy_point[1] - xy[1])**2)
        d.append(dist)
        
    return d

xy_points = [[3,2], [2,3], [2,2]]
xy = [1,2]
dist_2_points(xy_points, xy)
