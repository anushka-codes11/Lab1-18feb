# Sample list of student scores
scores = [28, 32, 45, 38, 30, 50, 33, 20, 40]

# Step 1: Remove the lowest 2 scores
scores.sort()  # Sort ascending
scores = scores[2:]  # Remove first 2 (lowest) scores

# Step 2: Add 5 marks to scores between 30 and 35 (inclusive)
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Step 3: Count number of students who passed (>=40)
passed_count = sum(1 for score in scores if score >= 40)

print("Processed Scores:", scores)
print("Number of students passed:", passed_count) 