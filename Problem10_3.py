def compute_commission_and_target(sales):
  # Determine commission rate based on sales amount
  if sales > 100000:
      commission = sales * 0.10
  else:
      commission = sales * 0.05

  # Calculate next year's target as 5% of the current sales
  next_year_target = sales * 0.05
  return commission, next_year_target

def main():
  # Input salesperson's last name
  last_name = input("Enter the salesperson's last name: ")

  # Input total sales
  sales = float(input("Enter total sales: "))

  # Compute commission and next year's target
  commission, next_year_target = compute_commission_and_target(sales)

  # Display results
  print(f"\nSalesperson's Last Name: {last_name}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${next_year_target:.2f}")

if __name__ == "__main__":
  main()
