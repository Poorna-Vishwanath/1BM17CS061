class Student:
    def __init__(self,sid,marks,age):
        self.sid=sid
        self.marks=marks
        self.age=age
    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            print("Valid marks")
        else:
            print("Invalid marks")

    def validate_age(self):
        if(self.age>20):
            print("Valid age")
        else:
            print("Invalid age")
    def check(self):
        if self.marks>65 and self.age>20: 
            print("Qualified")
        else:
            print("Not Qualified")
    def display(self):
        print("Student ID=",self.sid)
        print("Marks=",self.marks)
        print("Age=",self.age)

a=Student(61,72,2)

b=a.validate_marks()
c=a.validate_age()
a.display()
a.check()


        
