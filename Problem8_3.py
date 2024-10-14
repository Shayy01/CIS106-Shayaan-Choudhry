def compute_mpg(miles_travelled, gallons_used):
  # Calculate miles per gallon; handle division by zero
  if gallons_used == 0:
      return 0.0
  return miles_travelled / gallons_used

def main():
  trip_count = 0

  while True:
      # Get user input for destination city, miles, and gallons
      destination_city = input("Enter the destination city: ")

      try:
          miles_travelled = float(input("Enter miles traveled: "))
          gallons_used = float(input("Enter gallons used: "))
      except ValueError:
          print("Invalid input. Please enter numeric values for miles and gallons.")
          continue

      # Compute miles per gallon
      mpg = compute_mpg(miles_travelled, gallons_used)

      # Display destination c
