def compute_total(quantity, price):
  total = quantity * price
  # Apply a 10% discount if total is over $10,000.00
  if total > 10000:
      total *= 0.90  # Apply 10% discount
  return total

def main():
  extended_price = 0
  while True:
      # Get user input for quantity and price
      try:
          quantity = int(input("Enter the quantity: "))
          price = float(input("Enter the price per item: "))
      except ValueError:
          print("Invalid input. Please enter numeric values for quantity and price.")
          continue

      # Compute the total
      total = compute_total(quantity, price)

      # Display quantity, price, and total
      print(f"Quantity: {quantity}, Price per item: ${price:.2f}, Total: ${total:.2f}")

      # Update the extended price
      extended_price += total

      # Ask if the user wants to continue
      continue_program = input("Do you want to enter another quantity and price? (Yes or No): ").strip().lower()
      if continue_program != 'yes':
          break

  # Display the extended price
  print(f"Extended Price: ${extended_price:.2f}")

if __name__ == "__main__":
  main()
