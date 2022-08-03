class School:
    def __init__(self):
        print("School Name : XXXXXXXXXXXXX")


class Class(School):
    def __init__(self):
        # super(Class, self).__init__()
        super().__init__() # super().Class Name
        print("Class : 2")


c = Class()

