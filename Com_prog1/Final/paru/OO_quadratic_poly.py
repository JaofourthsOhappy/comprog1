from OO_fraction import Fraction
from OO_complex import Complex
class QuadraticPoly:
    """This is a class for quadratic polynomial that has the form

    (a)*x^2 + (b)*x + (c)

    where a, b, and c are coefficients, x is a variable, and the ^ symbol stands for exponentiation, i.e., x^3 = x*x*x.

    The coefficients all have to be the same type, which can be Complex, Fraction, integer, float, or any type that supports basic arithmetic operations such as addition, subtraction, or multiplication.
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, other):
        """Return a new quadratic polynomial where coefficients of the terms with the same degree are added together. For example:

        if self is (1)*x^2 + (2)*x + (3) and other is (4)*x^2 + (5)*x + (6), then self.add(other) is (5)*x^2 + (7)*x + (9)
        """
        new_co_a = self.a+other.a
        new_co_b = self.b+other.b
        new_co_c = self.c+other.c
        return QuadraticPoly(new_co_a,new_co_b,new_co_c)


    def __add__(self, other):
        return self.add(other)
    
    def constant_multiply(self, const):
        """Return a new quadratic polynomial where each coefficient is multiplied by a constant given in const. """

        new_co_a = self.a * const
        new_co_b = self.b* const
        new_co_c = self.c*const
        return QuadraticPoly(new_co_a,new_co_b,new_co_c)

    def __str__(self):
        return f"({self.a})*x^2 + ({self.b})*x +({self.c})"

# """
# First operand: (1)*x^2 + (2)*x + (3)
# Second operand: (4)*x^2 + (5)*x + (6)
# First + Second = (5)*x^2 + (7)*x + (9)
# """
# first = QuadraticPoly(1,2,3)
# second = QuadraticPoly(4,5,6)
# print(first+second)

# """
# First operand: (1)*x^2 + (2)*x + (3)
# Constant: 4
# Constant * First = (4)*x^2 + (8)*x + (12)
# """
# first = QuadraticPoly(1,2,3)
# constant = 4
# print(first.constant_multiply(constant))

# """
# First operand: (1/2)*x^2 + (1/3)*x + (2/5)
# Second operand: (2/7)*x^2 + (5/4)*x + (6/5)
# First + Second = (11/14)*x^2 + (19/12)*x + (8/5)
# """
# first = QuadraticPoly(Fraction(1,2),Fraction(1,3),Fraction(2,5))
# second = QuadraticPoly(Fraction(2,7),Fraction(5,4),Fraction(6,5))
# print(first+second)

# """
# First operand: (1/2)*x^2 + (1/3)*x + (2/5)
# Constant: 2/7
# Constant * First = (1/7)*x^2 + (2/21)*x + (4/35)
# """
# first = QuadraticPoly(Fraction(1,2),Fraction(1,3),Fraction(2,5))
# constant = Fraction(2,7)
# print(first.constant_multiply(constant))

# """
# First operand: (1.1 + 2.2j)*x^2 + (3.3 + 4.4j)*x + (0.1 + 0.3j)
# Second operand: (5.5 + 6.6j)*x^2 + (7.7 + 8.8j)*x + (1.5 + 1.6j)
# First + Second = (6.6 + 8.8j)*x^2 + (11.0 + 13.200000000000001j)*x + (1.6 + 1.9000000000000001j)
# """
# first = QuadraticPoly(Complex(1.1,2.2),Complex(3.3,4.4) ,Complex(0.1,0.3))
# second = QuadraticPoly(Complex(5.5,6.6) , Complex(7.7,8.8) , Complex(1.5,1.6))
# print(first+second)

# """
# First operand: (1.1 + 2.2j)*x^2 + (3.3 + 4.4j)*x + (0.1 + 0.3j)
# Constant: 5.5 + 6.6j
# Constant * First = (-8.469999999999999 + 19.36j)*x^2 + (-10.89 + 45.980000000000004j)*x + (-1.4299999999999997 + 2.31j)
# """
# first = QuadraticPoly(Complex(1.1,2.2) ,Complex(3.3,4.4) , Complex(0.1,0.3))
# constant = Complex(5.5,6.6)
# print(first.constant_multiply(constant))


# """
# Coefﬁcient type is Complex whose real and imaginary parts are Fraction: 
# First operand: (1/2 + 1/3j)*x^2 + (1/3 + 1/6j)*x + (2/5 + 2/7j) 
# Second operand: (1/4 + 1/11j)*x^2 + (3/4 + 3/5j)*x + (5/4 + 6/5j) 
# First + Second = (3/4 + 14/33j)*x^2 + (13/12 + 23/30j)*x + (33/20 + 52/35j)
# """
# first = QuadraticPoly(Complex(Fraction(1,2),Fraction(1,3)) ,Complex(Fraction(1,3),Fraction(1,6)) , Complex(Fraction(2,5),Fraction(2,7)))
# second = QuadraticPoly( Complex (Fraction(1,4),Fraction(1,11)), Complex(Fraction(3,4), Fraction(3,5)), Complex(Fraction(5,4),Fraction(6,5)))
# print(first+second)

# """
# First operand: (1/2 + 1/3j)*x^2 + (1/3 + 1/6j)*x + (2/5 + 2/7j) 
# Constant: 1/4 + 1/11j 
# Constant * First = (25/264 + 17/132j)*x^2 + (3/44 + 19/264j)*x + (57/770 + 83/770j)
# """
# first = QuadraticPoly(Complex(Fraction(1,2),Fraction(1,3)) ,Complex(Fraction(1,3),Fraction(1,6)) , Complex(Fraction(2,5),Fraction(2,7)))
# constant = Complex(Fraction(1,4),Fraction(1,11))
# print(first.constant_multiply(constant))