
# Student Grade Management System

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")

    student_name = input("Enter student name: ").strip()
    while not student_name:
        print("Name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    marks = []
    number_of_subjects = 5

    for i in range(number_of_subjects):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark. Enter a value from 0 to 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = sum(marks) / len(marks)
    letter_grade = get_letter_grade(average)

    print("\n--- STUDENT RESULTS ---")
    print("Student Name:", student_name)
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark:.2f}")
    print(f"Average Mark: {average:.2f}")
    print("Letter Grade:", letter_grade)


if __name__ == "__main__":
    main()
