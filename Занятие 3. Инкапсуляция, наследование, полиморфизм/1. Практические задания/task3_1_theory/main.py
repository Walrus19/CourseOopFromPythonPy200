class Parent:
    @property
    def value(self):
        return "Value from Parent"

class Child(Parent):
    @property
    def value(self):
        return super().value + " and Value from Child"

child = Child()
print(child.value)  # Value from Parent and Value from Child

