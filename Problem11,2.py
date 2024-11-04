# Array of last names and their corresponding exam scores
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
              "Davis", "Miller", "Wilson", "Moore", "Taylor"]
exam_scores = [85, 92, 78, 88, 76, 95, 89, 84, 91, 73]

def display_names_and_scores(names, scores):
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

def display_names_and_scores_reverse(names, scores):
    for name, score in zip(reversed(names), reversed(scores)):
        print(f"{name}: {score}")

# Display names and scores and their reverse order
print("Names and Scores:")
display_names_and_scores(last_names, exam_scores)
print("\nNames and Scores in reverse order:")
display_names_and_scores_reverse(last_names, exam_scores)
