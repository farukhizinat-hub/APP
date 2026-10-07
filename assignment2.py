def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("         STUDENT REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class Report:
    college = "MIT ADT University, Pune"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    def __str__(self):
        return (f"Name     : {self.name}\n"
                f"Roll No  : {self.roll}\n"
                f"Marks    : {self.marks}")

    @report_header
    def display_report(self):
        print(f"College  : {Report.college}")
        print(self)

        if self.marks >= 40:
            print("Result   : PASS")
        else:
            print("Result   : FAIL")



name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
marks = int(input("Enter Marks: "))


student = Report(name, roll, marks)


student.display_report()


choice = input("\nDo you want to change the college name? (yes/no): ")

if choice.lower() == "yes":
    new_college = input("Enter New College Name: ")
    Report.change_college(new_college)

    print("\nUpdated Report:")
    student.display_report()