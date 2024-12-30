def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {price:.2f}")
