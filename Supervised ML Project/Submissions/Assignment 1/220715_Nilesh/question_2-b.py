import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Oranges']
quantities = [25, 40, 30]

# Plotting
plt.bar(categories, quantities)

# Labels and title
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')

# Display the graph
plt.show()