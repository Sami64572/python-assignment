class Student:
    def __init__(self, name, roll_number, subjects, marks):
        self.name, self.roll_number, self.subjects, self.marks = name, roll_number, subjects, marks

    def calculate_grade(self):
        avg_marks = sum(self.marks) / len(self.marks)
        return 'A' if avg_marks >= 90 else 'B' if 80 <= avg_marks < 90 else 'C' if 70 <= avg_marks < 80 else 'D' if 60 <= avg_marks < 70 else 'F'

student1 = Student("Alice", "S001", ["Math", "English", "Science"], [95, 88, 92])
student2 = Student("Bob", "S002", ["Math", "English", "Science"], [75, 82, 68])

for student in [student1, student2]:
    print(f"{student.name} (Roll Number: {student.roll_number}) - Grade: {student.calculate_grade()}")