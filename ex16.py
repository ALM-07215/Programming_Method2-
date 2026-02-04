import numpt as np
import random
rng = np.random.default_rng()
matrix = rng.random((5, 5)) 
print(f"Matrix:{matrix.mean():.2f},Std dection:{matrix.std():.2f}")
print(f"Row matrix:{matrix.max(axis=1)}")