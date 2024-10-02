"""
You are a data analyst at a company that tracks the monthly sales and expenses of two
different product lines over a year. You need to visualize this data to identify trends and make
informed decisions.
You have the following monthly sales data (in thousands) for Product A and Product B:
 Sales Data:
o Product A: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
o Product B: [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
And the following monthly expenses data (in thousands):
 Expenses Data:
o Product A: [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
o Product B: [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
You need to create a 2x2 subplot layout that shows:
1. Sales of Product A
2. Sales of Product B
3. Expenses of Product A
4. Expenses of Product B
"""
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

sales_a = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
sales_b = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
expenses_a = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
expenses_b = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

def sales_expenses_subplots():
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(221) # Sales of Product A
    ax2 = fig.add_subplot(222) # Sales of Product B
    ax3 = fig.add_subplot(223) # Expenses of Product A
    ax4 = fig.add_subplot(224) # Expenses of Product B

    # Product A Sales
    ax1.plot(range(1 ,13), sales_a, marker='o', color='blue')
    ax1.set_title('Sales of Product A')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales (in thousands)')
    ax1.set_xticks(range(1 ,13))

    # Product B Sales
    ax2.plot(range(1 ,13), sales_b, marker='o', color='green')
    ax2.set_title('Sales of Product B')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Sales (in thousands)')
    ax2.set_xticks(range(1 ,13))

    # Product A Expenses
    ax3.plot(range(1 ,13), expenses_a, marker='*', color='blue')
    ax3.set_title('Expenses of Product A')
    ax3.set_xlabel('Month')
    ax3.set_ylabel('Expenses (in thousands)')
    ax3.set_xticks(range(1 ,13))

    # Product B Expenses
    ax4.plot(range(1 ,13), expenses_a, marker='*', color='green')
    ax4.set_title('Expenses of Product A')
    ax4.set_xlabel('Month')
    ax4.set_ylabel('Expenses (in thousands)')
    ax4.set_xticks(range(1 ,13))

    fig.tight_layout()
    fig.savefig("outputs/exp-1-b.png")