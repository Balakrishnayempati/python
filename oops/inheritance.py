class Calculator:
    def __init__(Self):
        print("This is calculator constructor")
        
    def add(self):
        print("This is add")
    def sub(self):
        print("This is sub")
class Adcalculator(Calculator):
    def add(self):
        super().add()
        super().sub()
        print("This is advance add")
    def sub(self):
        print("This is advance sub")
    
cal1=Adcalculator()
cal1.add()
cal1.sub()