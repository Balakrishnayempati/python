class Dog:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def dogg(self):
        return f"Dog name is {self.name} amd sounds like {self.sound}"
d1=Dog("Lab","Bow Bow")
print(d1.dogg())
    
