# Attendance Tracking System

attendance = {}  # Dictionary to store student attendance


# Function to mark attendance
def mark_attendance():
    name = input("Enter student name: ").strip()
1
    if name in attendance:
        print("Attendance already marked for this student.")
    else:
        status = input("Enter attendance (Present/Absent): ").strip().lower()

        if status == "present" or status == "absent":
            attendance[name] = status
            print(f"Attendance recorded for {name}.")
        else:
            print("Invalid input. Please enter 'Present' or 'Absent'.")


# Function to view all attendance records
def view_attendance():
    if not attendance:
        print("No attendance records found.")
    else:
        print("\n--- Attendance Records ---")
        for name, status in attendance.items():
            print(f"{name}: {status}")
        print("--------------------------")


# Function to count attendance summary
def attendance_summary():
    present_count = 0
    absent_count = 0

    for status in attendance.values():
        if status == "present":
            present_count += 1
        elif status == "absent":
            absent_count += 1

    print("\n--- Attendance Summary ---")
    print(f"Present: {present_count}")
    print(f"Absent: {absent_count}")
    print("--------------------------")


# Main program loop
def main():
    while True:
        print("\n===== Attendance Tracking System =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Attendance Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            attendance_summary()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
main()