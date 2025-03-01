COLOR_TO_CODE = {
    'beige': '#f5f5dc',
    'cadetblue': '#5f9ea0',
    'chartreuse': '#7fff00',
    'coral': '#ff7f50',
    'cornflowerblue': '#6495ed',
    'darkgoldenrod': '#b8860b',
    'firebrick': '#b22222',
    'forestgreen': '#228b22',
    'gold': '#ffd700',
    'hotpink': '#ff69b4'
}

color = input('Color: ').lower()
while color != '':
    try:
        print(COLOR_TO_CODE[color])
    except KeyError:
        print('Invalid color or unrecorded color')
    color = input('Color: ').lower()
