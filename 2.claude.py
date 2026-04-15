import numpy as np

# From a Python list
a = np.array([1, 2, 3, 4, 5])
print(a, a.dtype)

# 2-D array (matrix)
matrix = np.array([[1, 2, 3],[4, 5, 6]])
print(matrix.shape)        

# Zeros, ones, identity
z = np.zeros((3, 3))
o = np.ones((2, 4), dtype=np.float32)
eye = np.eye(3)           # 3×3 identity matrix

# Range & linspace
r = np.arange(0, 10, 2)   # [0 2 4 6 8]
ls = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]

# Random arrays
rng = np.random.default_rng(seed=42)
rand = rng.random((3, 3))   # uniform [0, 1)
norm = rng.normal(loc=0, scale=1, size=1000)

# Reshaping
flat = np.arange(12)
grid = flat.reshape(3, 4) # shape (3, 4)
back = grid.ravel()       # back to 1-D