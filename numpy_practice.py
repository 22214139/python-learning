import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers)
print(numbers * 2)
print("sum:", np.sum(numbers))
print("average:", np.mean(numbers))
print("max:", np.max(numbers))
print("min:", np.min(numbers))
image = np.array([
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]
])
print(image)
print("shape:", image.shape)
zeros = np.zeros((3, 3))
print(zeros)

ones = np.ones((2, 4))
print(ones)