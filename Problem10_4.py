def compute_averages(game_scores, handicap):
  # Calculate average score
  average_score = sum(game_scores) / len(game_scores)
  # Calculate average score with handicap
  average_with_handicap = average_score + handicap
  return average_score, average_with_handicap

def main():
  # Input bowler's last name
  last_name = input("Enter the bowler's last name: ")

  # Input three game scores
  scores = []
  for i in range(3):
      score = float(input(f"Enter score for game {i + 1}: "))
      scores.append(score)

  # Input handicap
  handicap = float(input("Enter handicap: "))

  # Compute averages
  average_score, average_with_handicap = compute_averages(scores, handicap)

  # Display results
  print(f"\nBowler's Last Name: {last_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Average Score with Handicap: {average_with_handicap:.2f}")

if __name__ == "__main__":
  main()
