def calculate_bonus(salary):
  if salary >= 100000:
      return salary * 0.20
  elif salary >= 50000:
      return salary * 0.15
  else:
      return salary * 0.10

def main():
  total_bonus = 0.0

  with open("employees.txt", "r") as file:
      lines = file.readlines()

      for i in range(0, len(lines), 2):
          last_name = lines[i].strip() 
          salary = float(lines[i + 1].strip()) 

          bonus = calculate_bonus(salary)
          total_bonus += bonus

          print(f"Employee: {last_name}, Salary: ${salary:,.2f}, Bonus: ${bonus:,.2f}")

  print(f"\nTotal bonuses paid out: ${total_bonus:,.2f}")

if __name__ == "__main__":
  main()