def calculate_discount(quantity, price, discount_rate):
  total_price = quantity * price
  discount_amount = total_price * (discount_rate / 100)
  discounted_price = total_price - discount_amount
  return discount_amount, discounted_price

def main():
  # Input values
  quantity = float(input("Enter quantity: "))
  price = float(input("Enter price per item: "))
  discount_rate = float(input("Enter discount rate (in %): "))

  # Calculate discount and discounted price
  discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)

  # Display results
  print(f"Quantity: {quantity}")
  print(f"Price per item: {price}")
  print(f"Discount Amount: {discount_amount:.2f}")
  print(f"Discounted Price: {discounted_price:.2f}")

if __name__ == "__main__":
  main()
