class Student():
    name="기본값"
    age=0
    def __init__(self, name, age):
        self.name=name

    def show(self):
        print(Student.name + "  asdfsdaf  "+self.name)

s1 = Student("승우",26)
s1.show()
