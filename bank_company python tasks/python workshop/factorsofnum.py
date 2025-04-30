number=int(input("Enter any numbers:"))
for i in range(1,number+1):
    if number%i==0:
        print("divisible by",i)