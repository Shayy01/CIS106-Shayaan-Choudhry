def compute_batting_average(hits, at_bats):
  # Calculate batting average; handle division by zero
  if at_bats == 0:
      return 0.0
  return hits / at_bats

def main():
  player_count = 0

  while True:
      # Get user input for last name, hits, and at-bats
      last_name = input("Enter player's last name: ")

      try:
          hits = int(input("Enter number of hits: "))
          at_bats = int(input("Enter number of at-bats: "))
      except ValueError:
          print("Invalid input. Please enter numeric values for hits and at-bats.")
          continue

      # Compute the batting average
      batting_average = compute_batting_average(hits, at_bats)

      # Display last name and batting average
      print(f"Player: {last_name}, Batting Average: {batting_average:.3f}")

      # Increment the player count
      player_count += 1

      # Ask if the user wants to continue
      continue_program = input("Do you want to enter another player? (Yes or No): ").strip().lower()
      if continue_program != 'yes':
          break

  # Display the number of players entered
  print(f"Total number of players entered: {player_count}")

if __name__ == "__main__":
  main()
