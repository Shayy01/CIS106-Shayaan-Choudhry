# Array of last names and scores
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
              "Davis", "Miller", "Wilson", "Moore", "Taylor"]
exam_scores = [85, 92, 78, 88, 76, 95, 89, 84, 91, 73]

def find_highest_score(scores):
    high_var = 0
    high_index = -1
    for i, score in enumerate(scores):
        if score > high_var:
            high_var = score
            high_index = i
    return high_index

def find_lowest_score(scores):
    low_var = 999
    low_index = -1
    for i, score in enumerate(scores):
        if score < low_var:
            low_var = score
            low_index = i
    return low_index

highest_index = find_highest_score(exam_scores)
lowest_index = find_lowest_score(exam_scores)

print(f"Highest Score: {last_names[highest_index]}: {exam_scores[highest_index]}")
print(f"Lowest Score: {last_names[lowest_index]}: {exam_scores[lowest_index]}")

