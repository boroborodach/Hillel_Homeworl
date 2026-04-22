class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if isinstance(other, Fraction):
            denominator = max(self.b, other.b)
            while denominator % self.b != 0 and denominator % other.b != 0:
                denominator += 1
            new_a = self.a + (0 if denominator == self.b else denominator / self.b)
            new_b = other.a + (0 if denominator == other.b else denominator / other.b)
            return Fraction(int(new_a + new_b), denominator)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            denominator = max(self.b, other.b)
            while denominator % self.b != 0 and denominator % other.b != 0:
                denominator += 1
            new_a = self.a + (0 if denominator == self.b else denominator / self.b)
            new_b = other.a + (0 if denominator == other.b else denominator / other.b)
            return Fraction(int(new_a - new_b), denominator)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return not self.__lt__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
