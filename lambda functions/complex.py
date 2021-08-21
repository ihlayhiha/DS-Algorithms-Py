class Complex:

    def __init__(self, re, im) -> None:
        self.re = re
        self.im = im

    
    def __add__(self, value):
        if isinstance(value, (float, int)):
            afterAdd = Complex(self.re + value, self.im)
            return afterAdd
            # return (self.re + value, self.im)
        elif isinstance(value, complex):
            afterAdd = Complex(self.re + value.real, self.im + value.imag)
            return afterAdd
            # return (self.re + value.real, self.im + value.imag)
        elif isinstance(value, Complex):
            afterAdd = Complex(self.re + value.re, self.im  + value.im)
            return afterAdd
            # return (self.re + value.re, self.im + value.im)

    def  __gt__(self, other):
        if isinstance(other, Complex):
            vector1 = ((self.re)**2 + (self.im)**2)**(1/2)
            vector2 = ((other.re)**2 + (other.im)**2)**(1/2)
            if vector1 > vector2:
                return True
            return False
        elif isinstance(other, (int, float)):
            vector1 = ((self.re)**2 + (self.im)**2)**(1/2)
            if vector1 > other:
                return True
            return False
        elif isinstance(other, complex):
            vector1 = ((self.re)**2 + (self.im)**2)**(1/2)
            vector2 = (other.real**2 + other.imag**2)**(1/2)
            if vector1 > vector2:
                return True
            return False

    def __str__(self):
        return f"({self.re}, {self.im})"




randComplex = Complex(1, 2)
another = Complex(2, 3)

print(randComplex)

print(randComplex + 10)
print(randComplex + complex(1, 2))
print(randComplex + another)

addedStuff = randComplex + another
print(addedStuff.re)

print(randComplex > another)
print(another > 1)

print(randComplex)
print(another)
