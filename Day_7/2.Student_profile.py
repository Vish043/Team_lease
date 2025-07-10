# Takes input from user
#-> Student id
#->Student Name
#->Dictionary type Subject Name and marks
#->Calculate_Grades()
#->generate report

class Student_details:
    def __init__(self,id,name,subject):
        self.id = id
        self.name = name
        self.subject = subject
        self.total = 0
        self.average = 0
        self.grade = ""

    def calculate_grades(self):
        self.total = sum(self.subject.values())
        self.average = self.total/len(self.subject)

        if self.average >= 90:
            self.grade = "A+"
        elif self.average >=80:
            self.grade = "A"
        elif self.average >=70:
            self.grade = "B"
        elif self.average >=60:
            self.grade = "C"
        elif self.average >=50:
            self.grade = "D"
        else:
            self.grade = "F"

    def generate_report(self):
        print("\n----- Student Report -----")
        print(f"Student ID   : {self.id}")
        print(f"Name         : {self.name}")
        print("Subjects and Marks:")
        for subject,marks in self.subject.items():
            print(f"{subject}:{marks}")
        print(f"Total Marks : {self.total}")
        print(f"Average     : {self.average}")
        print(f"Grade       : {self.grade}")
        print("--------------------------")

student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
subjects = {}
num_subjects = int(input("Enter number of Subjects: "))
for _ in range (num_subjects):
    subject_name = input("Enter subject name: ")
    marks = float(input(f"Enter marks for {subject_name}: "))
    subjects[subject_name] = marks

student = Student_details(student_id, name, subjects)

student.calculate_grades()
student.generate_report()


