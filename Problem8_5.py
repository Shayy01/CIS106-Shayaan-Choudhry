def compute_tuition_owed(credit_hours, district_code):
  # Determine tuition rate based on district code
  if district_code == 'I':
      return credit_hours * 250  # In-district rate
  elif district_code == 'O':
      return credit_hours * 550  # Out-of-district rate
  else:
      return 0  # Invalid district code

def main():
  total_tuition = 0
  while True:
      # Get user input for last name, credit hours, and district code
      last_name = input("Enter student's last name: ")

      try:
          credit_hours = int(input("Enter credit hours: "))
          district_code = input("Enter district code (I for in-district, O for out-of-district): ").strip().upper()
      except ValueError:
          print("Invalid input. Please enter numeric values for credit hours.")
          continue

      # Compute tuition owed
      tuition_owed = compute_tuition_owed(credit_hours, district_code)

      if tuition_owed == 0:
          print("Invali
