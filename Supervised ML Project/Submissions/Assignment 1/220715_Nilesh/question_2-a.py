import matplotlib.pyplot as plt

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [150, 200, 180, 220, 250, 230]

# Plotting
plt.plot(years, sales, marker='o')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Sales (in millions)')
plt.title('Sales Trend')

# Display the graph
plt.show()