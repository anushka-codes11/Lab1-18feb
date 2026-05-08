# Sample product stock quantities
stock = [0, 5, 12, 8, 0, 20, 3]

# Step 1: Remove items with 0 stock
stock = [qty for qty in stock if qty != 0]

# Step 2: Add 50 units to items with stock below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Step 3: Calculate total inventory count
total_inventory = sum(stock)

print("Updated Stock Quantities:", stock)
print("Total Inventory Count:", total_inventory)