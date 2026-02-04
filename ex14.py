import numpy as np
raw_accel=np.array([[0.1,0.1,9.9],[0.1,0.1,9.9],[0.2,0.0,9.8],[0.1,0.2,9.9]])
bias=np.array([0.1,0.1,9.8])
clean_accel=raw_accel-bias
new_accel=clean_accel*9.81
print(new_accel)