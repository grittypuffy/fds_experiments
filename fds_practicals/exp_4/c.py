"""
A teacher wants to analyze the relationship between her students' scores in Math and
Science based on their performance. She records the following scores:
 Math: Alice (88), Bob (76), Charlie (95), David (67), Eva (89), Frank (82)
 Science: Alice (92), Bob (80), Charlie (85), David (70), Eva (90), Frank (75)
Using a scatter plot with text annotations for each student, what insights can the teacher gain
from this visualization?
"""
import os
import matplotlib.pyplot as plt

def students_scatter_plot():
        
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
    math_scores = [88, 76, 95, 67, 89, 82]
    science_scores = [92, 80, 85, 70, 90, 75]
    plt.figure(figsize=(8, 6))
    plt.scatter(math_scores, science_scores, color='blue', s=100, edgecolor='black')
    for i, student in enumerate(students):
        plt.text(math_scores[i] + 0.5, science_scores[i] + 0.5, student, fontsize=10)

    plt.title("Math vs Science Scores of Students")
    plt.xlabel("Math Scores")
    plt.ylabel("Science Scores")

    plt.xlim(60, 100)
    plt.ylim(60, 100)

    plt.grid(True)
    plt.savefig(os.path.join("outputs", "exp-4-c.png"))