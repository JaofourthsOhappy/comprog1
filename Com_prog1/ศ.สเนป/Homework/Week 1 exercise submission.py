#1
def total_seconds(hour,minute,second):
    return (hour*3600)+(minute*60)+second
#2
import math
def circle_circumference(r):
    return 2*math.pi *r

#3
def future_value(present_value,annual_rate,years):
    m = (present_value * (annual_rate+1))**years
    return m

#4
import math
def point_distance(x0,y0,x1,y1):
    d = math.sqrt(((x0-x1)**2)+((y0-y1)**2)) 
    return d
#5
import math
def point_distance(x0,y0,x1,y1):
    d = math.sqrt(((x0-x1)**2)+((y0-y1)**2)) 
    return d
def triangle_area ():
    a = point_distance(x0,y0,x1,y1)
    b = point_distance(x1,y1,x2,y2) 
    c = point_distance(x2,y2,x0,y0)
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
    

#6
def print_digits(num):
    ten = num//10
    one = num % 10
    print(f"The tens digit is {ten}, and the ones digit is {one}.")

