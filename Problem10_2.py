def compute_scores(exam_scores):
  # Calculate total points
  total_points = sum(exam_scores)
  # Calculate average score
  average_score = total_points / len(exam_scores)
  return total_points, average_score

def main():
  # Input student's last name
  last_name = input("Enter the student's last name: ")

  # Input three exam scores
  scores = []
  for i in range(3):
      score = float(input(f"Enter score for exam {i + 1}: "))
      scores.append(score)

  # Compute total points and average score
  total_points, average_score = compute_scores(scores)

  # Display results
  print(f"\nStudent's Last Name: {last_name}")
  print(f"Total Points: {total_points:.2f}")
  print(f"Average Exam Score: {average_score:.2f}")

if __name__ == "__main__":
  main()
