def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


num_subjects = int(input("Enter the number of subjects: "))


marks = []
for i in range(num_subjects):
    mark = float(input(f"Enter the marks for subject {i + 1}: "))
    marks.append(mark)


total, average = calculate_total_and_average(marks)


print("\nMarks entered:")
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")