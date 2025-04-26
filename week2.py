map = open('/Users/ababeiteodor/Desktop/python/YEAR2/small.txt')
trailheads = []
height_1 = []
height_2 = []
height_3 = []
height_4 = []
height_5 = []
height_6 = []
height_7 = []
height_8 = []
summit = []
i = 0
for line in map:
    j = 0
    for height in line:
        if height == '0':
            trailheads.append([i, j])
        if height == '1':
            height_1.append([i, j])
        if height == '2':
            height_2.append([i, j])
        if height == '3':
            height_3.append([i, j])
        if height == '4':
            height_4.append([i, j])
        if height == '5':
            height_5.append([i, j])
        if height == '6':
            height_6.append([i, j])
        if height == '7':
            height_7.append([i, j])
        if height == '8':
            height_8.append([i, j])
        if height == '9':
            summit.append([i, j])
        j += 1
    i += 1

def getnext(coords, value):
    ''' For each coordinate in 'coords', find and return the
    coordinates of the adjacent cells that contain 'value'
    '''
    newcoords = []
    # Iterate over coords and check adjacent cells
    # Add the coords of the cells containing 'value' to newcoords
    return newcoords