import functions as fnc

main = fnc.introduction()
start = fnc.shade_colour_search(main)
num = fnc.shade_number(main, start)
main_arc = fnc.arc_main_colors(main)
arc = fnc.combination(main_arc, num)
main_triangle = fnc.triangle_main_colors(main)
triangle = fnc.combination(main_triangle, num)
main_square = fnc.square_main_colors(main)
square = fnc.combination(main_square, num)

print('\nMain arc colors:', main_arc)
print('Arc shades:', arc)
print('\nMain triangle colors:',main_triangle)
print('Triangle shades:', triangle)
print('\nMain square colors:', main_square)
print('Square shades:', square)
print('\n')