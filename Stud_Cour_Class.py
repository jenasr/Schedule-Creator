class StudentCourse:
    req = "General Education"
    def __init__(self, name, term, units, grade):
        self.name = name
        self.term = term
        self.units = units
        self.grade = grade

    def info(self):
        return "{} {} {} {} {}".format(self.term, self.name, self.units, self.grade, self.req)

    
