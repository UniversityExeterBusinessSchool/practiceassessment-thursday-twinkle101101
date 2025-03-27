#######################################################################################################################################################
# 
# Name:Twinkle Chauhan
# SID:750015322
# Exam Date:27 March 2025
# Module:progamming for business analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-twinkle101101
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

# Given customer feedback text
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Initialize an empty list to store (start, end) positions
my_list = []

# Your allocated keys (first and last digit of SID)
allocated_keys = [7, 2]  # From SID: first=7, last=2

# Iterate through allocated keys and find their positions in text
for key in allocated_keys:
    word = key_comments[key]  # Get the word using the key
    start_pos = customer_feedback.find(word)  # Find the start position
    if start_pos != -1:  # If the word is found
        end_pos = start_pos + len(word)  # Calculate the end position
        my_list.append((start_pos, end_pos))  # Append as a tuple

# Print the results
print(my_list)
#output
#[(129, 136), (114, 120)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
# Function to calculate Operating Profit Margin
def operating_profit_margin(profit, revenue):
    if revenue == 0:
        return "Revenue cannot be zero."
    return (profit / revenue) * 100

# Function to calculate Revenue per Customer
def revenue_per_customer(total_revenue, num_customers):
    if num_customers == 0:
        return "Number of customers cannot be zero."
    return total_revenue / num_customers

# Function to calculate Customer Churn Rate
def customer_churn_rate(customers_lost, total_customers):
    if total_customers == 0:
        return "Total customers cannot be zero."
    return (customers_lost / total_customers) * 100

# Function to calculate Average Order Value (AOV)
def average_order_value(total_revenue, num_orders):
    if num_orders == 0:
        return "Number of orders cannot be zero."
    return total_revenue / num_orders

# Inputs using SID digits
profit = 75  # First two digits
revenue = 220  # Last two digits multiplied by 10 for realistic revenue
customers_lost = 22  # Last two digits
total_customers = 150  # Arbitrary example
num_customers = 75  # First two digits
num_orders = 44  # Arbitrary example

# Calling the functions
op_margin = operating_profit_margin(profit, revenue)
rev_per_cust = revenue_per_customer(revenue, num_customers)
churn_rate = customer_churn_rate(customers_lost, total_customers)
aov = average_order_value(revenue, num_orders)

# Display results
print(f"Operating Profit Margin: {op_margin:.2f}%")
print(f"Revenue per Customer: ${rev_per_cust:.2f}")
print(f"Customer Churn Rate: {churn_rate:.2f}%")
print(f"Average Order Value: ${aov:.2f}")
#output
#Operating Profit Margin: 34.09%
#Revenue per Customer: $2.93
#Customer Churn Rate: 14.67%
#Average Order Value: $5.00
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Train a linear regression model
model = LinearRegression()
model.fit(prices, demand)

# Get regression coefficients
slope = model.coef_[0]  # Rate of change of demand per price unit
intercept = model.intercept_  # Base demand when price is zero

# Define the revenue function: Revenue = Price × Demand
def revenue(price):
    demand_pred = slope * price + intercept  # Predict demand
    return price * demand_pred  # Revenue formula

# Find the price that maximizes revenue
optimal_price = -intercept / (2 * slope)

# Predict demand when price = £52
price_52 = 52
demand_52 = model.predict(np.array([[price_52]]))[0]

# Display results
print(f"Optimal Price to Maximize Revenue: £{optimal_price:.2f}")
print(f"Predicted Demand at £52: {demand_52:.0f} units")

# Plot demand vs price
plt.scatter(prices, demand, color='blue', label="Actual Data")
plt.plot(prices, model.predict(prices), color='red', label="Regression Line")
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.legend()
plt.title("Price vs Demand Regression")
plt.show()
#output
#Optimal Price to Maximize Revenue: £43.65
#Predicted Demand at £52: 158 units
##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

import random
import matplotlib.pyplot as plt

# Get student ID and generate 100 random numbers
max_value = int(input("Enter your Student ID: "))  # Fixed variable name and input conversion
random_numbers = [random.randint(1, max_value) for _ in range(100)]  # Use _ instead of unused variable

# Plotting the numbers in a line chart
plt.plot(
    random_numbers, 
    marker='o', 
    markerfacecolor='green', 
    markeredgecolor='red', 
    linestyle='--', 
    label='Random Numbers', 
    color='blue'
)

# Fixing title and labels
plt.title("Line Chart of 100 Random Numbers")  # String inside quotes
plt.xlabel("Index")  # Use function call
plt.ylabel("Random Number")

# Fixing legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

