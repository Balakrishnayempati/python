from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def Check_balance(self):
        pass
    @abstractmethod
    def Deposit(self):
        pass
    @abstractmethod
    def Withdrawl(self):
        pass
class SBI(ATM):
    def Check_balance(self):
        print("0 balance in sbi bank")
    def Deposit(self):
        print("1000 rupees deposited in sbi bank")
    def Withdrawl(self):
        print("500 withdrawl from sbi bank")

class ICICI(ATM):
    def Check_balance(self):
        print("0 balance in sbi bank")
    def Deposit(self):
        print("1000 rupees deposited in sbi bank")
    def Withdrawl(self):
        print("500 withdrawl from sbi bank")

sb=SBI()
ic=ICICI()
