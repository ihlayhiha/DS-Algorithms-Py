class A:

    def __init__(self) -> None:
        print("This constructor will run even when u create only it's child classes when the child class do not have a constructor")

    @staticmethod
    def checker():
        print("This is just a checker")

    @classmethod
    def info(cls):
        print("This is more about class A")

    def feature1(self):
        print("Feature1 working fine")

    def feature2(self):
        print("Feature2 working fine")

class B:

    @classmethod
    def info(cls):
        print("this is more about class B")


    def __init__(self) -> None:
        print("Defining a new constructor that can override the constructor of its superclass")
        # super().__init__()

    def feature2(self):
        # super().feature2()   # calling the feature class from top before executing what ever is there in this method
        print("This is a feature from class B")



class C(A, B):

    def __init__(self) -> None:
        super().__init__()

    def feat(self):
        super().feature2()

# a = A()
# a.info()
# A.info()
# a.feature2()
# A.checker()
# a.checker()

# B.checker()
# b = B()
# b.info()
# b.info()
# b.checker()
# b.feature2()

c = C()
c.feature1()
c.feat() 