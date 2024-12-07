class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code.upper()  # Ensure the district code is case-insensitive
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      # Determine tuition rate based on district code
      if self.district_code == 'I':
          rate_per_credit = 250.00
      else:
          rate_per_credit = 500.00
      # Compute total tuition
      return self.enrolled_credits * rate_per_credit


# Test the class
student1 = Student('John', 'Doe', 'I', 12)  # In-district student with 12 credits
student2 = Student('Jane', 'Smith', 'O', 15)  # Out-of-district student with 15 credits

# Display student details and tuition
print(f"Student: {student1.first_name} {student1.last_name}")
print(f"District Code: {student1.district_code}")
print(f"Enrolled Credits: {student1.enrolled_credits}")
print(f"Tuition Owed: ${student1.compute_tuition():.2f}\n")

print(f"Student: {student2.first_name} {student2.last_name}")
print(f"District Code: {student2.district_code}")
print(f"Enrolled Credits: {student2.enrolled_credits}")
print(f"Tuition Owed: ${student2.compute_tuition():.2f}")
