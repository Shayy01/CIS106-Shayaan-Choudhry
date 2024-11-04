# Array of last names
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
              "Davis", "Miller", "Wilson", "Moore", "Taylor"]

def display_names(names):
    for name in names:
        print(name)

def display_names_reverse(names):
    for name in reversed(names):
        print(name)

# Display names and their reverse order
print("Names:")
display_names(last_names)
print("\nNames in reverse order:")
display_names_reverse(last_names)
