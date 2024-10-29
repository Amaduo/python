def get_grade(marks):
    match marks:

        case marks if 80 <= marks < 100:
            return "A"
        case marks if 60 <= marks < 79:
            return "B"
        case marks if 40 <= marks < 59:
            return "C"
        case marks if 0 <= marks < 39:
            return "D"
        case _:
            return "Invalid marks"


marks = int(input("Enter the student's marks: "))
grade = get_grade(marks)
print(f"The student's grade is: {grade}")

