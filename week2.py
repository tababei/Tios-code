#Read the file and transform it in accessible format
map = open('/Users/ababeiteodor/Desktop/python/YEAR2/small.txt')
trailheads = []
text = map.read()
lines = text.splitlines()

# Find trailheads
i = 0
for line in lines:
    j = 0
    for height in line:
        if height == '0':
            trailheads.append([i, j])
        j += 1
    i += 1



def getnext(coords, value):
    ''' For each coordinate in 'coords', find and return the
    coordinates of the adjacent cells that contain 'value'
    '''
    x, y = coords
    
    newcoords = []
    # Iterate over coords and check adjacent cells
    # Add the coords of the cells containing 'value' to newcoords
    return newcoords