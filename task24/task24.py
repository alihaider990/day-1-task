class Attendance:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.attendance = []

    def mark_attendance(self, status):
        status = status.upper()  
        if status in ("P", "A"):
            self.attendance.append(status)
            if status == "P":
                print(f"{self.name} is present")
            else:
                print(f"{self.name} is absent")
        else:
            print("Invalid status. Use p for present and a for absent")

    def attendance_percentage(self):
        total = len(self.attendance)
        if total == 0:
            return None
        present = self.attendance.count("P")
        percentage = (present / total) * 100
        return percentage

    def below_75(self):
        percentage = self.attendance_percentage()
        return percentage is not None and percentage < 75

    def display_attendance(self):
        print(f"Student id: {self.id}")
        print(f"Student name: {self.name}")
        print(f"Attendance: {self.attendance}")
        percentage = self.attendance_percentage()
        if percentage is None:
            print("No attendance record yet.")
        else:
            print(f"Attendance percentage: {percentage:.2f}%")
            if percentage < 75:
                print("Attendance below 75% and he was absent in rest of classes")
            else:
                print("Attendance is sufficient.")


students = [
    Attendance(1, "Ali"),
    Attendance(2, "Haider"),
    Attendance(3, "Hassan"),
    Attendance(4, "Ismail")
]


marking_attendance = ["p", "P", "a", "A"]

for student, mark in zip(students, marking_attendance):
    student.mark_attendance(mark)
    student.display_attendance()


print("\nStudents those attandance is below 75%:")
for student in students:
    if student.below_75():
        print(f"{student.name} ({student.id}) - {student.attendance_percentage():.2f}%")

        #time complexcity is 0(1) bacuase we are checking each student one by one