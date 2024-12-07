class Employee:
  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'

  def bonus(self, rate):
      return float(rate) * float(self.pay)


# Instantiate the object
emp1 = Employee('Frank', 'Alvino', 60000.00)

# Display employee details
print(f"Email: {emp1.email}")
print(f"First Name: {emp1.first}")
print(f"Last Name: {emp1.last}")
print(f"Salary: {emp1.pay}")

# User input for bonus rate
bonus_rate = float(input("Enter the bonus rate (e.g., 0.10 for 10%): "))
bonus_amount = emp1.bonus(bonus_rate)

# Display the computed bonus
print(f"Bonus at rate {bonus_rate}: {bonus_amount:.2f}")
