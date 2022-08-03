class Student:
    roll = ""
    age = ""

    def set_value(self, roll, age):
        self.roll = roll
        self.age = age

    def display(self):
        print(f"Roll : {self.roll}, AGE : {self.age}")


rahim = Student()
rahim.set_value(101, 15)
rahim.display()

kamal = Student()
kamal.set_value(102, 15.6)
kamal.display()

