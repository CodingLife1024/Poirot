class Mathematics:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return a ** b

    def root(self, a, b):
        return a ** (1/b)

    def factorial(self, a):
        if a == 0:
            return 1
        else:
            return a * self.factorial(a-1)