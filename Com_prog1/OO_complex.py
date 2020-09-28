class Complex:
    def __init__(self, re, im):
        """Must heck if re and im are of the same types"""
        self.re = re
        self.im = im

    def add(self, m):
        num_re = self.re + m.re 
        num_im = self.im + m.im
        c = Complex(num_re,num_im)
        return c
    
    def __add__(self, m):
        return self.add(m)

    def subtract(self, m):
        num_re = self.re - m.re
        num_im = self.im - m.im 
        c = Complex(num_re,num_im)
        return c   
    def __sub__(self, m):
        return self.subtract(m)
    
    def multiply(self, n):
        num_re = (self.re * n.re) - (self.im * n.im)
        num_im = (self.re*n.im) + (self.im * n.re)
        c = Complex(num_re,num_im)
        return c
    
    def __mul__(self, n):
        return self.multiply(n)

    def __str__(self):
        return str(self.re) + ' + ' + str(self.im) + 'j'
