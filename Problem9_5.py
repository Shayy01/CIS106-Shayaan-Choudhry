def compute_assessed_value(county, market_value):
  """Determine the assessed value based on county and market value."""
  assessed_value_percent = {
      "Cook": 0.90,
      "DuPage": 0.80,
      "McHenry": 0.75,
      "Kane": 0.60
  }.get(county, 0.70)  # Default to 0.70 for all other counties

  assessed_value = market_value * assessed_value_percent
  return assessed_value

def main():
  total_market_value = 0
  total_assessed_value = 0

  while True:
      user_input = input("Would you like to enter home data? (Yes or No): ").strip().lower()
      if user_input == 'yes':
          county = input("Enter the county: ")
          market_value = float(input("Enter the market value of the home: "))

          assessed_value = compute_assessed_value(county, market_value)
          total_market_value += market_value
          total_assessed_value += assessed_value

          print(f"The assessed value for the home in {county} is: ${assessed_value:.2f}")
      elif user_input == 'no':
          print("Thank you for using the home assessment calculator!")
          break
      else:
          print("Invalid input. Please enter 'Yes' or 'No'.")

  print(f"\nTotal market value of all homes: ${total_market_value:.2f}")
  print(f"Total assessed value of all homes: ${total_assessed_value:.2f}")

if __name__ == "__main__":
  main()
