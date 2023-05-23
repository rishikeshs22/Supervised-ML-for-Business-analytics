import numpy as np

# Generate a random 4x4 matrix
matrix = np.random.randint(1, 10, size=(4, 4))
print("Original Matrix:\n", matrix)

#  the transpose of the matrix
transpose = np.empty_like(matrix)
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        transpose[j][i] = matrix[i][j]
print("Transpose Matrix:\n", transpose)

# Perform matrix multiplication
result = np.zeros((4, 4))
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        for k in range(matrix.shape[0]):
            result[i][j] += matrix[i][k] * transpose[k][j]
print("Matrix Multiplication Result:\n", result)

# Reshape the result matrix to a 2x8 matrix
reshaped = np.reshape(result, (2, 8))
print("Reshaped Matrix:\n", reshaped)