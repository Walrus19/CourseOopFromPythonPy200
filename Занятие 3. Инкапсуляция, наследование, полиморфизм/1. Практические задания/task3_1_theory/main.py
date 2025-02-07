class Parent:
    def __init__(self):
        self._value = "Initial Value"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Child(Parent):
    @property
    def value(self):
        return super().value.upper()

    @value.setter
    def value(self, new_value):  # наследование сеттра достаточно специфично
        super(Child, type(self)).value.__set__(self, new_value + " (modified)")

child = Child()
child.value = "New Value"
print(child.value)  # NEW VALUE (MODIFIED)

