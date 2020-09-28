import OO_complex
import OO_fraction
import OO_quadratic_poly

def test_quadratic_poly_add(x, y):
    print("First operand: ", end='')
    print(x)
    print("Second operand: ", end='')
    print(y)
    print("First + Second = ", end='')
    print(x + y)

def test_quadratic_poly_constant_mult(x, const):
    print("First operand: ", end='')
    print(x)
    print("Constant: ", end='')
    print(const)
    print("Constant * First = ", end='')
    print(x.constant_multiply(const))

c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
qp1 = OO_quadratic_poly.QuadraticPoly(c1, c2, c3)
qp2 = OO_quadratic_poly.QuadraticPoly(c4, c5, c6)
test_quadratic_poly_add(qp1, qp2)
print()
test_quadratic_poly_constant_mult(qp1, c4)
print()

# I also test result in OO_quadratic_poly.py too