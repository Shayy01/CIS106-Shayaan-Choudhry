#Input phase
student_count = 0
continue_program = input("Do you want to enter student data? (Yes/No): ")
#Process phase
while continue_program == 'yes':

    last_name = input("Enter your last name: ")

    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))

    average_score = (score1 + score2) / 2
#Output phase       
print(f"Last Name: {last_name}, Average Score: {average_score:.2f}")

student_count += 1

continue_program = input("Do you want to enter data for another student? (Yes/No): ")

print(f"Total number of students who entered data: {student_count}")