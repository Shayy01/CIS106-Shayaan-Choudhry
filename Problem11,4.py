# Load player names and batting averages from a file
last_names = []
batting_averages = []

with open('players.txt', 'r') as file:
    for line in file:
        name, average = line.strip().split(',')
        last_names.append(name)
        batting_averages.append(float(average))

def display_players(names, averages):
    for name, average in zip(names, averages):
        print(f"{name}: {average}")

def search_player(name, names, averages):
    if name in names:
        index = names.index(name)
        return names[index], averages[index]
    return None

# Display players
print("Players and their Batting Averages:")
display_players(last_names, batting_averages)

# User input for searching
while True:
    search_name = input("Enter a last name to search (or 'exit' to quit): ")
    if search_name.lower() == 'exit':
        break
    result = search_player(search_name, last_names, batting_averages)
    if result:
        print(f"Found: {result[0]} with batting average: {result[1]}")
    else:
        print("Name not found.")
