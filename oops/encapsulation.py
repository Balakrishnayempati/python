class HumanBeing:
    def __init__(self,name,gender,dob):
        self.__name=name
        self._gender=gender
        self.dob=dob
        print("Human object created")
    def introduce(self):
        print(self.__name,self.dob)


    def get_name(self):
        return self.__name
        
    def set_name(self,new_name):
        self.__name=new_name
        print("Name changed")
        
    
h1=HumanBeing("babu","Male","24 feb")
# print(h1.name)
# print(h1.gender)
# print(h1.dob)
# h1.name="baba"
# print(h1.name)
print(h1._gender)  #public
print(h1.__name)  #private