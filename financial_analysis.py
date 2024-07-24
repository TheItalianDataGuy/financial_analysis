import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Financial Datasets
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44,
           11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20,
            3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Gross profit for each month
gross_profit = {}
for i in range(0, len(revenue)):
    gross_profit[months[i]] = f"${round(revenue[i] - expenses[i])}"

print(gross_profit)

# Create the graph of the Revenue/expenses
plt.plot(
    months,
    list(np.round(revenue)),
    label="Revenue")

plt.plot(
    list(gross_profit.keys()),
    list(np.round(expenses)),
    label="Expenses")

plt.title("Financial Dataset")
plt.xlabel('Months')
plt.ylabel('US Dollars ($)')
plt.legend()
plt.show()

# Create a graph of the Gross Profit
fig = px.line(
    x=list(gross_profit.keys()),
    y=[float(value.replace("$", "")) for value in gross_profit.values()],
    labels={"x": "Months", "y": "US Dollars ($)"},
    title="Gross Profit")
fig.show()

# Profit after tax
profit_after_tax = {}

for i in range(0, len(gross_profit.values())):
    value = float(list(gross_profit.values())[i].strip('$'))
    profit_after_tax[months[i]] = f"${(round(value - (value * 0.3)))}"

print(profit_after_tax)

# Profit margin for each month
profit_margin = {}
for i in range(0, len(profit_after_tax.values())):
    value = float(list(profit_after_tax.values())[i].strip("$"))
    profit_margin[months[i]] = (f'{round((value / revenue[i]) * 100)}%')

print(profit_margin)

# Transform profit_after_tax into an array
profit = profit_after_tax.items()
profit_list = list(profit)
profit_array = np.array(profit_list)

# Get just the values from the array (comprehension list when a specific element of a list is needed)
items = [item[1] for item in profit_array]
dollars = [int(item.strip("$")) for item in items]
dollars_array = np.array(dollars)
print(dollars_array)

# Calculate good months and bad months
dollars_mean = round(dollars_array.mean())
print(dollars_mean)

good_months = {}
bad_months = {}

for i, dollar in enumerate(dollars_array):
    if dollar > dollars_mean:
        good_months[months[i]] = f"${dollar}"
    else:
        bad_months[months[i]] = f"${dollar}"

print("Good Months = ", good_months)
print("Bad Months = ", bad_months)
print(profit_array)

# Transform the element in the array into integers
profit_values = profit_array[:, 1].astype(str)
profit_values = [int(item.strip("$")) for item in profit_values]
profit_values = np.array(profit_values)
print(profit_values)

# Calculate the good month
# Get the index
max_index = np.argmax(profit_values)
# Find the profit in that index
good_month = f"${profit_values[max_index]}"
# Find the month in that index
month_max = months[max_index]

print("The good month is", month_max, "with", good_month)

# Calculate the bad month

# Get the index
min_index = np.argmin(profit_values)
# Find the profit in that index
good_month = f"${profit_values[min_index]}"
# Find the month in that index
month_min = months[min_index]

print("The good month is", month_min, "with", good_month)
