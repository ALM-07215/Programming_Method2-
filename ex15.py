import numpy as np
import random 
rng=np.random.default_rng(seed=42)
power_matrix=rng.random((4,5))*10

total_power=power_matrix.sum 
AveragrPower=power_matrix.min(axis=1)
PeakPower=power_matrix.max(axis=0)
time=power_matrix.T#Transpose matrix 
print(f"Total:{total_power}W\n New Shape:{time}")
