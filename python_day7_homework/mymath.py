# 삼각형 넓이
def triangle_area(base, height):
    area = 0.5 * base * height 
    return area

# 원의 넓이 
pi = 3.141592

def circle_area(radius):
    area = pi * (radius ** 2)
    return area

# 직육면체의 넓이
def rectangular_surface_area(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

