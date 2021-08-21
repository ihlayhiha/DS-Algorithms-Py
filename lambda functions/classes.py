class Student:

    School = "Whatever School"

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.School

    

print(Student.School)
print(Student.info())