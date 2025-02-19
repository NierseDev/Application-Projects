def input_student_data():
    students = {}

    print("""
Enter student grades (format: StudentName: Grade)
    
Press Enter twice to finish input
Press Ctrl+C to exit the program\n""")

    while True:
        try:
            data = input()

            if data == "":
                break

            name, grade = data.split(":")
            name = name.strip()
            grade = float(grade.strip())

            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                continue

            students[name] = grade
        except ValueError:
            print("Invalid input format. Please enter data in the format: StudentName: Grade.")  
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully...")
            return None
    return students

def calculate_statistics(students):
    if not students:
        return None

    total_students = len(students)
    grades = list(students.values())
    average_grade = sum(grades) / total_students
    highest_grade = max(grades)
    lowest_grade = min(grades)
    passing_count = sum(1 for grade in grades if grade >= 60)

    return {
        "total_students": total_students,
        "average_grade": average_grade,
        "highest_grade": highest_grade,
        "lowest_grade": lowest_grade,
        "passing_count": passing_count
    }

def display_results(students, stats):
    if not students:
        print("No student data entered.")
        return

    print(f"""
Results:
----------------------------------------
Number of students: {stats['total_students']}
Average grade: {stats['average_grade']:.2f}
Highest grade: {stats['highest_grade']}
Lowest grade: {stats['lowest_grade']}
Number of passing students: {stats['passing_count']}

Individual Grades:
----------------------------------------""")
    
    # Sorting the students by name in ascending order
    for name in sorted(students):
        grade = students[name]
        status = "PASSED" if grade >= 60 else "FAILED"
        print(f"{name}: {grade:.1f} ({status})")

def main():
    while True:
        try:
            students = input_student_data()
            if students is None:
                break
            stats = calculate_statistics(students)
            display_results(students, stats)
            break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully...")
            break

if __name__ == "__main__":
    main()
