# Ex.1
def total_seconds(hours,minutes,seconds):
    total_time = (hours*3600)+(minutes*60)+seconds
    return total_time
    
# Ex.2
import math
def circle_circumference(radius):
    circum = 2*math.pi*radius
    return circum

# Ex.3
def future_value(present_value,annual_rate,years):
    for i in range(0,years):
        present_value = (present_value*annual_rate)+present_value
    return present_value

# Ex.4
def point_distance(x0,y0,x1,y1):
    distance = math.sqrt(((x0-x1)**2)+((y0-y1)**2))
    return point_distance

# Ex.5
def point_distance(x0,y0,x1,y1):
    distance = math.sqrt(((x0-x1)**2)+((y0-y1)**2))
    return point_distance

def triangle_area(x0,y0,x1,y1,x2,y2):
    a = point_distance(x0,y0,x1,y1)
    b = point_distance(x1,y1,x2,y2)
    c = point_distance(x0,y0,x2,y2)
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area

# Ex.6
import sys
def print_digits(number):
    if 0 <= number < 100:
        print(f"The ten digit is {number//10}, and the one digit is {number%10}")
    else:
        sys.exit()