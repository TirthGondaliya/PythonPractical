def is_prime(a):
    if a < 2:
        return "Not Prime"
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return "Not Prime"
    return "Prime"


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    @staticmethod
    def area(length, width):
        return length * width


class Circle(Shape):
    @staticmethod
    def area(radius):
        return 3.14 * radius ** 2


class Triangle(Shape):
    @staticmethod
    def area(*args):
        if len(args) == 2:  # Base & Height
            base, height = args
            return 0.5 * base * height
        elif len(args) == 3:  # Three Sides (Heron's Formula)
            a, b, c = args
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        else:
            print("Invalid Number of Arguments!!!")
            return None
