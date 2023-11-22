
house_height = float(input())
side_length = float(input())
roof_side = float(input())

side_area = house_height * side_length
window_area = 1.5 * 1.5
sides_area = (2 * side_area) - (2 * window_area)

back_side = house_height * house_height
#entrance 2.4

back_front_area = (2 * back_side) - 2.4

house_area = sides_area + back_front_area
green_paint = house_area / 3.4

print(f'{green_paint:.2f}')

#roof

roof_area = 2 * (house_height * side_length)
roof_triangle =  (house_height * roof_side / 2)
roof_triangle = 2 * roof_triangle
roof_area_paint = roof_area + roof_triangle
red_paint = roof_area_paint / 4.3

print(f'{red_paint:.2f}')


