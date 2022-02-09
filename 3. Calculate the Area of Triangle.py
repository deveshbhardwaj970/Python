# def triangle_area(base, height):
#     return (base*height)/2
    
# base = float(input('Enter Base of Triangle : '))
# height = float(input('Enter Height of Triangle : '))
# print('Area of Triangle is ', triangle_area(base, height))

# By usins Lambda Function
triangle_area = lambda base, height : (base*height)/2

base = float(input('Enter Base of Triangle : '))
height = float(input('Enter Height of Triangle : '))
area = triangle_area(base, height)
print('Area of Triangle is ', round(area, 2))