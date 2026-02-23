# E-Commerce Cart System with Discount and GST

# Given list of product prices in cart
cart_prices = [1200, 2500, 1200, 800, 2500, 1500]

# Step 1: Remove duplicate items
unique_prices = list(set(cart_prices))

# Step 2: Calculate total
total = sum(unique_prices)

# Step 3: Apply discount if total > 5000
discount = 0
if total > 5000:
    discount = total * 0.10

amount_after_discount = total - discount

# Step 4: Add GST 18%
gst = amount_after_discount * 0.18
final_amount = amount_after_discount + gst

# Step 5: Display summary
print("---- Cart Summary ----")
print("Original Prices:", cart_prices)
print("Unique Prices:", unique_prices)
print(f"Total Amount: ₹{total:.2f}")
if discount > 0:
    print(f"Discount Applied (10%): ₹{discount:.2f}")
print(f"Amount after Discount: ₹{amount_after_discount:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Final Payable Amount: ₹{final_amount:.2f}")