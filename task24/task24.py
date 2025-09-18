class Attendance:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.attendance = []   

    def mark_attendance(self, status):
        if status in ("P", "A"):  
            self.attendance.append(status)
            if status == "P":
                print(f"{self.name} is present")
            else:
                print(f"{self.name} is absent")
        else:
            print("Invalid status and use p for present and A for absent")

    def attendance_percentage(self):   
        total = len(self.attendance)
        if total == 0:
            return None
        present = self.attendance.count("P")
        percentage = (present / total) * 100
        return percentage

    def below_75(self):
        percentage = self.attendance_percentage()
        return percentage < 75 

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

student=Attendance(1,"Ali")
student.mark_attendance("P")
student.display_attendance()

student2=Attendance(2,"haider")
student2.mark_attendance("P")
student2.display_attendance()

student3=Attendance(3,"hassan")
student3.mark_attendance("A")
student3.display_attendance()

student4=Attendance(4,"ismail")
student4.mark_attendance("A")
student4.display_attendance()   




# time complexity is O(n) because we are checking each student one by one   







        
