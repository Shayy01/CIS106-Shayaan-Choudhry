class Employee:
  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'

  def bonus(self, rate):
      return float(rate) * self.pay


class Manager(Employee):
  def long_term_bonus(self):
      return 0.40 * self.pay


# Test the Manager class
manager1 = Manager('Sarah', 'Conner', 120000.00)

# Display manager details and bonuses
print(f"Manager: {manager1.first} {manager1.last}")
print(f"Email: {manager1.email}")
print(f"Salary: ${manager1.pay:.2f}")
print(f"Regular Bonus (10%): ${manager1.bonus(0.10):.2f}")
print(f"Long Term Bonus (40%): ${manager1.long_term_bonus():.2f}")
