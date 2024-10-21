def get_forecast_percent(month):
  """Determine the forecast percent based on the month."""
  if month in ['Jan', 'Feb', 'Mar']:
      return 0.10
  elif month in ['Apr', 'May', 'Jun']:
      return 0.15
  elif month in ['Jul', 'Aug', 'Sep']:
      return 0.20
  elif month in ['Oct', 'Nov', 'Dec']:
      return 0.25
  else:
      return 0  # Default if month is invalid

def compute_forecast(month, sales):
  """Calculate next month's sales based on the forecast percent."""
  forecast_percent = get_forecast_percent(month)
  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

def main():
  while True:
      user_input = input("Would you like to enter sales data? (Yes or No): ").strip().lower()
      if user_input == 'yes':
          last_name = input("Enter last name: ")
          month = input("Enter month (e.g., Jan, Feb, etc.): ").strip()
          sales = float(input("Enter sales amount: "))

          next_month_sales = compute_forecast(month, sales)
          print(f"{last_name}, your forecasted sales for next month ({month}) are: ${next_month_sales:.2f}")
      elif user_input == 'no':
          print("Thank you for using the sales forecast program!")
          break
      else:
          print("Invalid input. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
  main()
