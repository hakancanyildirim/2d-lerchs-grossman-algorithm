block_dimension_x = input("Enter the number of blocks for the X dimension:")
block_dimension_y = input("Enter the number of blocks for the Y dimension:")

costs = float(input("Costs in dollars: "))
revenues = float(input("Revenues in dollars: "))

profit = costs - revenues

print("Here is your net profit: " + "$" + str(profit))