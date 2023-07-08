import numpy as np
import matplotlib.pyplot as plt

# Generate a random 4x4 matrix
matrix = np.random.rand(4, 4)

# Multiply the matrix with its transpose
result = np.matmul(matrix, matrix.T)

# Reshape the result to a 2x8 matrix
reshaped = result.reshape(2, 8)

# Plotting the three different types of graphs

# Line graph
plt.subplot(3, 1, 1)
plt.plot(reshaped[0, :], 'r-', label='Row 1')
plt.plot(reshaped[1, :], 'b-', label='Row 2')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Graph')
plt.legend()

# Bar graph
plt.subplot(3, 1, 2)
plt.bar(np.arange(8), reshaped[0, :], color='r', label='Row 1')
plt.bar(np.arange(8), reshaped[1, :], color='b', label='Row 2', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Graph')
plt.legend()

# Scatter plot
plt.subplot(3, 1, 3)
plt.scatter(np.arange(8), reshaped[0, :], color='r', label='Row 1')
plt.scatter(np.arange(8), reshaped[1, :], color='b', label='Row 2')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Scatter Plot')
plt.legend()

plt.tight_layout()
plt.show()
