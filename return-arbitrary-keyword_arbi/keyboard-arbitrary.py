def operation(num1,num2,**c):
    print(num1)
    print(num2)
    print(c)  #it prints in dictionary like and have **
operation(2,3,server='localhost',port='3308',password='123456',local='india')