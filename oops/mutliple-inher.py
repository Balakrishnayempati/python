class Lion:
    def roar(self):
        print("Lion is roar")
    def hunt(self):
        print("Lion is hunt")
    pass
class Tiger:
    # def roar(self):
    #     print("Tiger is roar")
    def hunt(self):
        print("Tiger is hunt")
    pass
class Liger(Tiger,Lion):
    def hunt(self):
        print("Liger is hunting")

lig=Liger()
lig.roar()
lig.hunt()

print(Liger.mro())
