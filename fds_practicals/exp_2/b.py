"""
 A teacher records the test scores of her students in a math exam as follows: [85, 90, 75, 85,
100, 90, 85, 80]. She wants to analyze the performance of her students. Calculate the mean,
median, and mode of these scores
"""

import numpy as np

def students_central_tendency():
    math_exam_marks = [85, 90, 75, 85, 100, 90, 85, 80]
    print(f"Mean: {np.mean(math_exam_marks)}")
    print(f"Median: {np.median(math_exam_marks)}")
    vals, counts = np.unique(math_exam_marks, return_counts=True)
    mode_value = np.argwhere(counts == np.max(counts))
    print(f"Mode: {vals[mode_value].flatten().tolist()}")
    