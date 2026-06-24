scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}
total_score = 0
for score in scores.values():
    total_score += score

average = total_score / len(scores)    
print(f"Class Average: {average}")

top_score = max(scores.values())
bottom_score = min(scores.values())

for name, score in scores.items():
    if score == top_score:
        print(f"Top Scorer: {name} with {score}")
    if score == bottom_score:    
        print(f"Bottom Scorer: {name} with {score}")

search_name = input("Enter a student name to search:")

result = scores.get(search_name, "Student not found in the records.")
print(f"Result: {result}")