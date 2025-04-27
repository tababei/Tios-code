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
    ''' 
    For each coordinate in 'coords', find and return the coordinates 
    of the adjacent cells that contain 'value'.
    '''
    newcoords = []
    for (x, y) in coords:
        # Check up
        if x > 0 and int(lines[x-1][y]) == value:
            newcoords.append((x-1, y))
        # Check down
        if x < len(lines)-1 and int(lines[x+1][y]) == value:
            newcoords.append((x+1, y))
        # Check left
        if y > 0 and int(lines[x][y-1]) == value:
            newcoords.append((x, y-1))
        # Check right
        if y < len(lines[0])-1 and int(lines[x][y+1]) == value:
            newcoords.append((x, y+1))
    return newcoords


total_popularity = 0

for head in trailheads:
    coords = [head]
    for height in range(1, 10):
        coords = getnext(coords, height)
    
    # Now coords contains all summits (height 9)
    unique_summits = set(coords)
    total_popularity += len(unique_summits)

print("Total Popularity Score:", total_popularity)