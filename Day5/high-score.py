student_scores = input().split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

max = student_scores[0]
for score in student_scores:
    if score>=max:
        max=score
print(f"Highest score is {max}")
