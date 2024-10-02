"""
A climate researcher is studying the temperature variations throughout the year in a specific
city. The researcher records the following average monthly temperatures (in °C): [5, 7, 10, 15,
20, 25, 30, 28, 22, 15, 10, 5]. Using this data, the researcher creates a line plot with a color bar.
What insights can the researcher gain from this visualization?
"""
import matplotlib.pyplot as plt
import numpy as np
import os

def temperature_line_plot():
    months = np.arange(1, 13)
    temperatures = np.array([5, 7, 10, 15, 20, 25, 30, 28, 22, 15, 10, 5])

    cmap = plt.get_cmap('coolwarm')
    norm = plt.Normalize(vmin=min(temperatures), vmax=max(temperatures))
    colors = cmap(norm(temperatures))

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(months, temperatures, c=temperatures, cmap='coolwarm', edgecolor='black')
    cbar = plt.colorbar(scatter)
    cbar.set_label('Temperature (°C)')

    plt.plot(months, temperatures, color='gray', linestyle='--', marker='o')
    plt.title('Average Monthly Temperature Variation')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.grid(True)
    plt.savefig(os.path.join("outputs", "exp-4-b.png"))