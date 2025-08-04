# Variables (lists for names and marks)
names = ["Ali", "hassan", "haider", "adnan"]
marks = [85, 92, 60, 35]


passed = 0
failed = 0

for i in range(len(names)):
    name = names[i]
    mark = marks[i]

    
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 60:
        grade = 'D'
    else:
        grade = 'F'

    
    if mark >= 60:
        passed += 1
    else:
        failed += 1

    
    print(f"{name} scored {mark} and got grade {grade}")

print(f"\nTotal Passed Students: {passed}")
print(f"Total Failed Students: {failed}")



