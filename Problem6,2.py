#Input phase 
start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
increment_value = int(input("Enter the increment value: "))
#Process phase
current_value = start_value
#Output phase
while current_value <= stop_value:
    print(current_value)
    current_value += increment_value