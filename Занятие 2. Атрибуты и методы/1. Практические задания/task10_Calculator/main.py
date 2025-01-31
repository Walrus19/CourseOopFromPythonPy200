class Calculator:
    # TODO Написать статический метод add для сложения двух чисел
    @staticmethod
    def mul(self, b):
    # TODO  Написать статический метод mul для умножения двух чисел
        return self * b

    @staticmethod
    def add(self, b):
        return self+b

if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
