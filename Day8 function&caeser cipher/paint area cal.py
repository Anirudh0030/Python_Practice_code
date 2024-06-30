import math

def paint_cal(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans}")
    
test_h = int(input("Height of wall: ")) # Height of wall (m)
test_w = int(input("width of wall: ")) # Width of wall (m)
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)
    