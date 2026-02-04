import numpy as np
period_1 = np.array([[10, 11, 12], [20, 21, 22]])
period_2 = np.array([[30, 31, 32], [40, 41, 42]])
full_data=np.vstack((period_1,period_2))
y_coordinate=full_data[:,1]
sub_matrix=full_data[2:,1:]
data_backup=full_data.copy()
print(f"Full shape:{full_data.shape}")
print(f"Submatrix:\n {sub_matrix}")
