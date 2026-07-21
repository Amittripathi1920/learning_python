student_scores = [3,20,14,25,16,78,45,12,12,43,63,59,24,85,61,2]
print(f"Total Sum (Func) : {sum(student_scores)}")

total_sum = 0
for score in student_scores:
    total_sum += score
print(f"Total Sum (Loop) : {total_sum}")

#Max
print(f"Max (Func) : {max(student_scores)}")

max_val = 0
for score in student_scores:
    if score > max_val:
        max_val = score

print(f"Max (Loop) : {max_val}")