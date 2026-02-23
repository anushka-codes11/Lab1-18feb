# Sample daily temperatures
temperatures = [38, 42, 46, 39, 50, 41, 44, 36]

# Step 1: Print "Heat Alert" for temperatures above 45°C
for temp in temperatures:
    if temp > 45:
        print(f"Temperature {temp}°C: Heat Alert!")

# Step 2: Count number of extreme days (>40°C)
extreme_days_count = sum(1 for temp in temperatures if temp > 40)

print("Number of extreme days (>40°C):", extreme_days_count)