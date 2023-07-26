# QAP 4 Monthly Sales Program
# Written By Zackery Walsh

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

# inputs
Jan = int(input("Enter total sales for January: "))
Feb = int(input("Enter total sales for February: "))
Mar = int(input("Enter total sales for March: "))
Apr = int(input("Enter total sales for April: "))
May = int(input("Enter total sales for May: "))
Jun = int(input("Enter total sales for June: "))
Jul = int(input("Enter total sales for July: "))
Aug = int(input("Enter total sales for August: "))
Sep = int(input("Enter total sales for September: "))
Oct = int(input("Enter total sales for October: "))
Nov = int(input("Enter total sales for November: "))
Dec = int(input("Enter total sales for December: "))

# Main Program
x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

y_axis = np.array(y_axis)

plt.plot(x_axis, y_axis)
plt.grid(True)

plt.title('Sales By Month')
plt.xlabel('Month')
plt.ylabel('Sales ($)')

plt.show()
