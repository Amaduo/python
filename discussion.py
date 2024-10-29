def calculate_total_average_grade(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 80 & average >= 90:
        grade = 'A'
    elif average >= 60 & average >= 79:
        grade = 'B'
    elif average >= 40 & average >= 59:
        grade = 'C'
    elif average >= 0 & average >= 60:
        grade = 'D'
    else:
        grade = 'Invalid'

    return total, average, grade



num_subjects = int(input("Enter the number of subjects: "))


marks = []
for i in range(num_subjects):
    mark = float(input(f"Enter the marks for subject {i + 1}: "))
    marks.append(mark)


total, average, grade = calculate_total_average_grade(marks)


print("\nMarks entered:")
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")