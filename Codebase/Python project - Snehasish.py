
#STUDENT GRADE CALCULATOR

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

while True:

    name = input("Enter student name: ")

    marks = []

    for i in range(5):

        while True:
            try:
                mark = float(input("Enter marks: "))

                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks. Enter marks between 0 and 100.")

            except ValueError:
                print("Invalid input. Enter numbers only.")

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("------------------------------")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Percentage: %.2f%%" % percentage)
    print("Grade:", grade)
    print("Result:", result)
    print("------------------------------")

    choice = input("Another student? (y/n): ")

    if choice == "n":
        print("Thank you!")
        break