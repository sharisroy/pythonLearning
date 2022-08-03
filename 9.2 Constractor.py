class Student:
    roll = ""
    age = ""

    # Constractor
    def __init__(self, roll, age):
        self.roll = roll
        self.age = age

    def display(self):
        print(f"Roll : {self.roll}, AGE : {self.age}")


haris = Student(101, 23)
haris.display()

kamal = Student(102, 32)
kamal.display()
