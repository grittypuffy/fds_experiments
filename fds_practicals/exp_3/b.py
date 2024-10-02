"""
 A fitness coach tracks the heights of his clients to analyze their body composition and overall
fitness. He records the following heights (in cm): [150, 160, 165, 170, 175, 180, 155, 165, 170,
175, 180, 190, 160, 165, 170, 175]. Using this data, he wants to visualize the distribution of
heights among his clients. What can he learn from the histogram generated from this dataset?
"""
import os
import matplotlib.pyplot as plt

def fitness_histogram():
    heights = [150, 160, 165, 170, 175, 180, 155, 165, 170, 175, 180, 190, 160, 165, 170, 175]

    plt.hist(heights, bins=range(150, 200, 5), edgecolor='black')
    plt.title('Distribution of Heights Among Clients')
    plt.xlabel('Height (cm)')
    plt.ylabel('Number of Clients')
    plt.xticks(range(150, 201, 5))
    plt.savefig(os.path.join("outputs", "exp-3-b.png"))