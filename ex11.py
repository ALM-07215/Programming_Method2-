import numpy as np 
raw_imu=np.array([0.1, 0.2, 9.8,
0.15, 0.22, 9.78, 0.12, 0.21, 9.81, 0.11, 0.23, 9.79],dtype=np.float64)
print(f"1D array: {raw_imu}")
print(f"Shape of array: {raw_imu.shape}")
print(f"Total size: {raw_imu.size} elements")
imu_matrix=raw_imu.reshape(4,3)
print(f"2D array:\n{imu_matrix}")
print(f"Shape of 2D array: {imu_matrix.shape}")
print(f"Total size: {imu_matrix.size} elements")
