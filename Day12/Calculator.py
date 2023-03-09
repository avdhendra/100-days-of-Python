
import math

def paint_calc(height,width,cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)
    print(f"You ll need {num_of_cans} can of paint")
    





test_height=int(input("Enter the Height of the wall"))
test_width=int(input("Enter the Width of the wall"))
coverage=5
paint_calc(height=test_height,width=test_width,cover=coverage)