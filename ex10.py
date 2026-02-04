import math
from datetime import datetime, time
arm_length = 1.5
target_angle_deg = 30.0
start_time = datetime.now()
target_angle_deg=math.radians(target_angle_deg)
y=arm_length*math.sin(target_angle_deg)
x=arm_length*math.cos(target_angle_deg)
print("the horizontal distance is: {x:.3f} meters".format(x=x))
print("the vertical height is: {y:.3f} meters".format(y=y))
duration = datetime.now() - start_time
print(f"Calculation took: {duration.total_seconds() * 10**6:.2f} microseconds")