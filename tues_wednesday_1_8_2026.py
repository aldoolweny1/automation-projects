def area_triangle(base, height):
	return base*height/2

area_a = area_triangle(6,8)
area_b = area_triangle(9,8)
area_c = area_triangle(3,4)
sum = area_a + area_b + area_c

print("The sum of the triangles is: " + str(sum))
