import numpy as np 
sensor_left=np.array([1.5, 0.8, 2.3])
sensor_right=np.array([2.1, 0.5, 1.9]) 
all_readings=np.concatenate((sensor_left,sensor_right))
print(f"All sensor readings: {all_readings}")
sorted_readings=np.sort(all_readings)
matrix=sorted_readings.reshape(2,3)
print(f"2D array of sorted readings:\n{matrix}")
