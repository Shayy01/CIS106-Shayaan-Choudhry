def main():
  while True:
#Input Phase
      principal = float(input("Enter principal amount: "))
      interest_rate = float(input("Enter interest rate (as a decimal, e.g., 0.10 for 10%): "))
#Process Phase
      total_interest = 0.0
      beginning_balance = principal
#Output Phase
      print("\nYear\tBeginning Balance\tEnding Balance")

      for year in range(1, 6):
          interest = beginning_balance * interest_rate
          ending_balance = beginning_balance + interest

          print(f"{year}\t${beginning_balance:,.2f}\t\t${ending_balance:,.2f}")

          total_interest += interest
          beginning_balance = ending_balance

      print(f"\nTotal interest earned: ${total_interest:,.2f}\n")

      cont = input("Do you want to enter another principal and interest rate? (yes/no): ")
      if cont.lower() != 'yes':
          break

if __name__ == "__main__":
  main()