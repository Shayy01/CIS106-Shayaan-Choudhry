def get_pay_rate(job_code):
  # Determine pay rate based on job code
  if job_code == 'L':
      return 25.00
  elif job_code == 'A':
      return 30.00
  elif job_code == 'J':
      return 50.00
  else:
      return 0.00  # Unknown job code

def compute_gross_pay(hours_worked, pay_rate):
  if hours_worked > 40:
      # Calculate overtime
      regular_pay = 40 * pay_rate
      overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
      return regular_pay + overtime_pay
  else:
      return hours_worked * pay_rate

def main():
  total_gross_pay = 0
  while True:
      # Get user input for last name, job code, and hours worked
      last_name = input("Enter employee's last name: ")
      job_code = input("Enter job code (L, A, or J): ").strip().upper()


