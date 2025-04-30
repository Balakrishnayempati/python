class Calculator:
    def __init__(Self):
        print("This is calculator constructor")
        
    def add(self):
        print("This is calulator add")
    def sub(self):
        print("This is calulator sub")
class Adcalculator(Calculator):
    def add(self):
        super().add()
        super().sub()
        print("This is advance_calulator add")
    def sub(self):
        print("This is advance_calulator sub")
class Supercalculator(Adcalculator):
    def add(self):
        super().add()
        super().sub()
        print("This is supercalulator add")
    def sub(self):
        print("This is supercalulator sub")

    
cal1=Supercalculator()
cal1.add()
cal1.sub()