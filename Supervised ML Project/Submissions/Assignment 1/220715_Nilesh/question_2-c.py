import matplotlib.pyplot as plt

# Data
categories = ['Red', 'Blue', 'Green', 'Yellow']
sizes = [30, 20, 40, 10]

# Plotting
plt.pie(sizes, labels=categories, autopct='%1.1f%%')

# Title
plt.title('Color Distribution')

# Display the graph
plt.show()