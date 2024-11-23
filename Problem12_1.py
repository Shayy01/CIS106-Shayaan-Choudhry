# 1. Prompt user for a number of items in a list, collect integers, and display the list
num_items = int(input("Enter the number of items in the list: "))
int_list = []

for i in range(num_items):
    value = int(input(f"Enter integer {i + 1}: "))
    int_list.append(value)

print("Initial list:", int_list)

# 2. Insert the score 99 at position 1 and display the list
int_list.insert(1, 99)
print("List after inserting 99 at position 1:", int_list)

# 3. Replace 99 with 100 and display the updated list
index_99 = int_list.index(99)
int_list[index_99] = 100
print("List after replacing 99 with 100:", int_list)

# 4. Create a second list, extend the first list with it, and display both
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
int_list.extend(second_list)
print("First list after extending with second list:", int_list)

# 5. Remove the value 800 and display the list
int_list.remove(800)
print("First list after removing 800:", int_list)

# 6. Remove the third item and display the list
del int_list[2]
print("First list after removing the third item:", int_list)

# 7. Create a grades list and perform operations
grades = ["A", "B", "C", "A", "A", "C"]
print("Grades list:", grades)

# 8. Display count of 'A' grades
count_a = grades.count("A")
print("Count of 'A' grades:", count_a)

# 9. Display the index of the first 'B' grade
index_b = grades.index("B")
print("Index of the first 'B' grade:", index_b)

# 10. Look for 'F' in the grades list and handle it gracefully
if "F" in grades:
    print("Grade 'F' found in the list.")
else:
    print("Grade 'F' is not in the list.")

# 11. Clear the second list and display it
second_list.clear()
print("Second list after clearing:", second_list)

# 12. Delete the second list and try displaying it (will cause an error)
del second_list
try:
    print(second_list)
except NameError:
    print("Second list has been deleted and no longer exists.")

# 13. Create a list of players and perform operations
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort the list of players and display it
players.sort()
print("Sorted players list:", players)

# 15. Make a copy of players called players2 and display it
players2 = players.copy()
print("Copy of players list (players2):", players2)

# 16. Reverse the order of players2 and display both lists
players2.reverse()
print("Original players list:", players)
print("Reversed players2 list:", players2)
