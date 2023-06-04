from data import mainColors

def introduction():
    '''( ) -> str

    The function asks about colour temperature and the one, returns it as the first palette color.
    '''

    temperature = input('Select a colour temperature, cold or warm: ')
    colours_half = int(len(mainColors) / 2)

    if temperature == 'warm':
        for i in range(colours_half):
            print(tuple(mainColors)[i])
        main_colour = input('Choose a color: ')
    elif temperature == 'cold':
        for i in range(colours_half, len(mainColors)):
            print(tuple(mainColors)[i])
        main_colour = input('Choose a color: ')
    else:
        print('Incorrect input')
    
    return main_colour

def shade_colour_search(mainColor):
    '''(str) -> str

    The function asks about shede of the colour and returns it as a start colour.
    '''
    
    for shade in mainColors[mainColor]:
        print(shade)
    
    shade_of_colour = input('Choose a color: ')

    return shade_of_colour

def shade_number(mainColor, colorShade):
    ''' (str, str) -> int

    The function returns a number of the selected color.
    '''

    number = mainColors[mainColor].index(colorShade)
    
    return number

def arc_main_colors(mainColor):
    ''' (str) -> tuple

    The function returns a tuple of colors to create a tuple of necessary shades.

    >>>arc_main_colors("Magenta")
    Magenta, Bougainvillea, Pink, Red plum
    '''

    wanted_colors_amount = 4
    arc_main_colors = tuple(mainColor.split())

    for i in range(len(mainColors)):

        i_color = tuple(mainColors)[i]

        if (i_color == mainColor):
            
            i_color_index = tuple(mainColors).index(i_color)
            end_color_index = i_color_index + wanted_colors_amount - 1
            correct_end_of_circle = end_color_index < len(mainColors)

            if correct_end_of_circle:
                for j in range(i_color_index + 1, end_color_index + 1):
                    arc_main_colors += tuple(tuple(mainColors)[j].split())
            else:
                if i_color_index + 1 != len(mainColors):
                    for k in range(i_color_index + 1, len(mainColors)):
                        arc_main_colors += tuple(tuple(mainColors)[k].split())
                    for k in range(0, wanted_colors_amount - len(arc_main_colors)):
                        arc_main_colors += tuple(tuple(mainColors)[k].split())
                elif i_color_index + 1 == len(mainColors):
                    for k in range(0, wanted_colors_amount - len(arc_main_colors)):
                        arc_main_colors += tuple(tuple(mainColors)[k].split())
            break

    return arc_main_colors

def triangle_main_colors(mainColor):
    ''' (str) -> tuple

    '''

    colors_step = 7
    i_color_index = tuple(mainColors).index(mainColor)
    one_way_index = i_color_index - colors_step - 1
    other_way_index = i_color_index + colors_step + 1

    if other_way_index + 1 > len(mainColors) - 1:
        other_way_index = one_way_index - colors_step - 1

    triangle_main_colors = tuple(mainColor.split())
    triangle_main_colors += tuple(tuple(mainColors)[one_way_index].split())
    triangle_main_colors += tuple(tuple(mainColors)[other_way_index].split())

    return triangle_main_colors

def square_main_colors(mainColor):
    ''' (str) -> tuple

    '''

    step = 5
    i_color_index = tuple(mainColors).index(mainColor)

    square_main_colors = tuple(mainColor.split()) # square_main_colors += tuple(tuple(mainColors)[i_color_index].split())
    i_color_index -= step + 1
    square_main_colors += tuple(tuple(mainColors)[i_color_index].split())
    i_color_index -= step + 1
    square_main_colors += tuple(tuple(mainColors)[i_color_index].split())
    i_color_index -= step + 1
    square_main_colors += tuple(tuple(mainColors)[i_color_index].split())

    return square_main_colors

def combination(MainColors, index):
    ''' (tuple, int) -> tuple

    '''

    colors = ()

    for color in MainColors:
        colors += tuple(mainColors[color][index].split())
    
    return colors

