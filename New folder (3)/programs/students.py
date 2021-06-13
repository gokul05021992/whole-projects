class StudentInfo:

    def get_info(self):
        name=input("Enter the Student name:")
        dept=input("Enter the student Department:")
        age=int(input("Enter Student Age:"))
        coll=input("Enter College name:")
        id=int(input("Enter Student ID:"))
        self.name=name
        self.dept=dept
        self.age=age
        self.coll=coll
        self.id=id

    def show_info(self):
        print("Student Name:",self.name)
        print("Student ID:",self.id)
        print("Student Age:",self.age)
        print("Student Department:",self.dept)
        print("Student College:",self.coll)

student = StudentInfo()
student.get_info()

