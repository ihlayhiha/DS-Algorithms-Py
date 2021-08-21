class Student:

    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno

    def show(self):
        print(f"Name: {self.name}, Roll No: self.{self.rollno}")
    
    class Laptop:

        def __init__(self, brand, ram, cpu) -> None:
            self.brand = brand
            self.ram = ram
            self.cpu = cpu

        def show(self):
            print(f"Laptop brand: {self.brand}, ram: {self.ram}, cpu: {self.cpu}")

me  = Student("yella", 23)
me.show()
laptop = Student.Laptop("Lenovo", "8GB", "i7")
laptop.show()   