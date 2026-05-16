# =================================
# School Management System
# Serial Number = Admission Order
# Roll Number = Rank Based on Total Marks
# =================================

welcome = "Welcome To School Management System"
print(welcome.center(80, "-"))

students = {}


# =================================
# Helper Function: Calculate Result
# =================================
def calculate_result(serial):
    marks = students[serial]["marks"]

    if len(marks) == 0:
        students[serial]["Total"] = 0
        students[serial]["Average"] = 0
        students[serial]["Percentage"] = 0
        students[serial]["Grade"] = ""
        students[serial]["Status"] = ""
        return

    total = sum(marks.values())
    avg = total / len(marks)
    percentage = (total / 800) * 100

    # Grade Calculation
    if 90 <= avg <= 100:
        grade = "Ex"
    elif 80 <= avg < 90:
        grade = "A"
    elif 70 <= avg < 80:
        grade = "B"
    elif 60 <= avg < 70:
        grade = "C"
    elif 50 <= avg < 60:
        grade = "D"
    else:
        grade = "F"

    # Pass / Fail
    if avg >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Store all result data
    students[serial]["Total"] = total
    students[serial]["Average"] = avg
    students[serial]["Percentage"] = percentage
    students[serial]["Grade"] = grade
    students[serial]["Status"] = status


# =================================
# Helper Function: Update Roll Numbers
# =================================
def update_roll_numbers():
    ranked_students = []

    for serial, data in students.items():
        ranked_students.append((serial, data["Total"]))

    # Sort by Total Marks (Highest First)
    ranked_students.sort(key=lambda x: x[1], reverse=True)

    roll = 1
    for serial, total in ranked_students:
        if total > 0:
            students[serial]["Roll"] = roll
            roll += 1
        else:
            students[serial]["Roll"] = None


# =================================
# Add Student
# =================================
def add_student():
    serial = max(students.keys(), default=0) + 1

    name = input("Enter Student Name: ")

    students[serial] = {
        "Name": name,
        "Roll": None,
        "Total": 0,
        "Average": 0,
        "Percentage": 0,
        "Grade": "",
        "Status": "",
        "marks": {}
    }

    print("\nStudent Successfully Added!\n")
    print(f"Serial Number: {serial}")


# =================================
# Show All Students
# =================================
def show_students():
    if len(students) == 0:
        print("\nNo Student Found!\n")
        return

    print("\n" + " STUDENT LIST ".center(50, "-"))

    for serial, data in sorted(students.items()):
        print(f"Serial Number: {serial}")
        print(f"Name: {data['Name']}")
        print("-" * 50)


# =================================
# Add Marks
# =================================
def add_marks():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    serial = int(input("Enter Serial Number: "))

    if serial not in students:
        print("\nStudent not found!\n")
        return

    subjects = [
        "First Language",
        "Second Language",
        "History",
        "Geography",
        "Physical Science",
        "Life Science",
        "Math",
        "IT"
    ]

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        students[serial]["marks"][subject] = mark

    # Calculate and store result
    calculate_result(serial)

    # Update rank-based roll numbers
    update_roll_numbers()

    print("\nMarks Added Successfully!\n")


# =================================
# Calculate Grade
# =================================
def grade_calculator():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    serial = int(input("Enter Serial Number: "))

    if serial not in students:
        print("\nStudent not found!\n")
        return

    if students[serial]["Total"] == 0:
        print("No marks added!")
        return

    data = students[serial]

    print(f"\nName: {data['Name']}")
    print(f"Roll Number: {data['Roll']}")
    print(f"Total Marks: {data['Total']}")
    print(f"Average: {data['Average']:.2f}")
    print(f"Percentage: {data['Percentage']:.2f}%")
    print(f"Grade: {data['Grade']}")
    print(f"Status: {data['Status']}")


# =================================
# Search Student
# =================================
def search_student():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    serial = int(input("Enter Serial Number: "))

    if serial not in students:
        print("\nStudent not found!\n")
        return

    data = students[serial]

    print(f"\nSerial Number: {serial}")
    print(f"Roll Number: {data['Roll']}")
    print(f"Name: {data['Name']}")

    if len(data["marks"]) == 0:
        print("\nNo marks added yet!\n")
    else:
        print("\nMarks:")
        for subject, mark in data["marks"].items():
            print(f"{subject}: {mark}")


# =================================
# Delete Student
# =================================
def delete_student():
    if len(students) == 0:
        print("\nNo student added to delete!\n")
        return

    serial = int(input("Enter Serial Number: "))

    if serial not in students:
        print("\nStudent not found!\n")
        return

    name = students[serial]["Name"]
    del students[serial]

    # Recalculate roll numbers
    update_roll_numbers()

    print(f"\nStudent {name} Deleted Successfully!\n")


# =================================
# Show Class Topper
# =================================
def show_topper():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    topper_serial = None

    for serial, data in students.items():
        if data["Roll"] == 1:
            topper_serial = serial
            break

    if topper_serial is None:
        print("\nNo marks available!\n")
        return

    data = students[topper_serial]

    print("\n" + " CLASS TOPPER ".center(50, "="))
    print(f"Serial Number: {topper_serial}")
    print(f"Roll Number: {data['Roll']}")
    print(f"Name: {data['Name']}")
    print(f"Total Marks: {data['Total']}")
    print(f"Percentage: {data['Percentage']:.2f}%")
    print(f"Grade: {data['Grade']}")
    print("=" * 50)


# =================================
# View Student Profile
# =================================
def view_student_profile():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    serial = int(input("Enter Serial Number: "))

    if serial not in students:
        print("\nStudent not found!\n")
        return

    data = students[serial]

    print("\n" + " STUDENT PROFILE ".center(60, "="))
    print(f"Serial Number : {serial}")
    print(f"Roll Number   : {data['Roll']}")
    print(f"Name          : {data['Name']}")

    if len(data["marks"]) == 0:
        print("No marks added yet!")
        print("=" * 60)
        return

    print("\nSubject-wise Marks:")
    for subject, mark in data["marks"].items():
        print(f"{subject}: {mark}")

    print("\nResult Summary:")
    print(f"Total Marks : {data['Total']}")
    print(f"Average     : {data['Average']:.2f}")
    print(f"Percentage  : {data['Percentage']:.2f}%")
    print(f"Grade       : {data['Grade']}")
    print(f"Status      : {data['Status']}")
    print("=" * 60)


# =================================
# Show Full Report (Sorted by Roll Number)
# =================================
def show_full_report():
    if len(students) == 0:
        print("\nNo student added!\n")
        return

    # Only students with valid roll number
    ranked = []

    for serial, data in students.items():
        if data["Roll"] is not None:
            ranked.append((serial, data))

    # Sort by Roll Number
    ranked.sort(key=lambda x: x[1]["Roll"])

    print("\n" + " FULL STUDENT REPORT ".center(80, "="))

    for serial, data in ranked:
        print(f"\nSerial Number : {serial}")
        print(f"Roll Number   : {data['Roll']}")
        print(f"Name          : {data['Name']}")

        print("\nSubject-wise Marks:")
        for subject, mark in data["marks"].items():
            print(f"{subject}: {mark}")

        print("\nResult Summary:")
        print(f"Total Marks : {data['Total']}")
        print(f"Average     : {data['Average']:.2f}")
        print(f"Percentage  : {data['Percentage']:.2f}%")
        print(f"Grade       : {data['Grade']}")
        print(f"Status      : {data['Status']}")
        print("-" * 80)

    print("=" * 80)


# =================================
# Main Menu
# =================================
while True:
    print("\n\n1. Add Student")
    print("2. Show All Students")
    print("3. Add Marks")
    print("4. Calculate Grade")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Show Class Topper")
    print("8. View Student Profile")
    print("9. Show Full Report")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        add_marks()
    elif choice == "4":
        grade_calculator()
    elif choice == "5":
        search_student()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        show_topper()
    elif choice == "8":
        view_student_profile()
    elif choice == "9":
        show_full_report()
    elif choice == "10":
        print("Thank you for using School Management System!")
        break
    else:
        print("Invalid choice! Please try again.")