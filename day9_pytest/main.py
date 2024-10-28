from lion.calculator import add, multi

class CalculatorClass:
    def __init__(self):
        pass

    def add(self, x, y):
        output = add(x, y)
        return output
    
cal = CalculatorClass()
output = cal.add(12, 90)
print(output)