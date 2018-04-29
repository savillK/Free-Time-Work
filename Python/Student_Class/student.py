class Student(object):
    def __init__(self, firstName, lastName, ID, GPA, school):
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID
        self.GPA = GPA
        self.school = school

  
    def check_GPA(self):
        if isinstance(self.GPA, float):
            if(self.GPA < 0.0 or self.GPA > 4.0):
                print("Invalid GPA, by default, your GPA will be set to 0.0")
                self.GPA = 0.0
                return False
            else:
                return True
        else:
            return False
    
    def check_id(self):
        if isinstance(self.GPA, int):
            return True
        else:
            return False

    def set_first(self, name):
        self.firstName = name

    def set_last(self, name):
        self.lastName = name

    def set_first(self, id):
        self.id = id

    def set_first(self, GPA):
        self.GPA = GPA

    def set_first(self, school):
        self.school = school

    def print_student(self):
        print "%s %s attends %s, currently has a GPA of %.1f, and has a student ID which is %d" % (self.firstName, self.lastName, self.school, self.GPA, self.ID)



s1 = Student("Stephen", "Hawking", 4493002, 4.0, "University of Cambridge")

s1.print_student()






