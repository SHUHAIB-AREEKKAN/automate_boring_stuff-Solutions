grid = [['.',
['.',
['O',
['O',
['.',
['O',
['O',
['.',
['.',
'.',
'O',
'O',
'O',
'O',
'O',
'O',
'O',
'.',
'.',
'O',
'O',
'O',
'O',
'O',
'O',
'O',
'.',
'.',
'.',
'O',
'O',
'O',
'O',
'O',
'.',
'.',
'.',
'.',
'.',
'O',
'O',
'O',
'.',
'.',
'.',
'.'],
'.'],
'.'],
'.'],
'O'],
'.'],
'.'],
'.'],
'.']]


for y in range(int(len(grid[0]))):    
    for x in range(int(len(grid))):
        print(grid[x][y], end='')
    print('\n')
