def main():
  total_gross_pay = 0
  employee_count = 0
#Input phase
  continue_program = input("Do you want to enter employee data? (Yes/No): ").strip().lower()

  while continue_program == 'yes':

      last_name = input("Enter employee last name: ")
      hours_worked = float(input("Enter hours worked: "))
      rate_of_pay = float(input("Enter rate of pay: "))

  #process phase
      if hours_worked > 40:
          regular_hours = 40
          overtime_hours = hours_worked - 40
          gross_pay = (regular_hours * rate_of_pay) + (overtime_hours * rate_of_pay * 1.5)
      else:
          gross_pay = hours_worked * rate_of_pay


      print(f"Employee Last Name: {last_name}, Gross Pay: ${gross_pay:.2f}")


      total_gross_pay += gross_pay
      employee_count += 1


      continue_program = input("Do you want to enter data for another employee? (Yes/No): ").strip().lower()

#Output phase
  if employee_count > 0:
      average_pay = total_gross_pay / employee_count
      print(f"\nTotal Gross Pay for all employees: ${total_gross_pay:.2f}")
      print(f"Total Number of Employees: {employee_count}")
      print(f"Average Pay: ${average_pay:.2f}")
  else:
      print("No employee data was entered.")

if __name__ == "__main__":
  main()