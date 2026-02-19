questions = [
    ("2+2", "4"),
    ("3+5", "8"),
    ("10-2", "8")
]

score = 0

for q, a in questions:
    ans = input(q + ": ")
    if ans == a:
        score += 1

print("Score:", score)
