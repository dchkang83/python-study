from scipy import interpolate

def test(x):
    x_points = [ 0, 1, 2, 3, 4, 5]
    y_points = [12,14,22,39,58,77]

    tck = interpolate.splrep(x_points, y_points)

    print("tck : ", tck)

    return interpolate.splev(x, tck)


print(test(1.25))

