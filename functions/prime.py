num=int(input("Enter any number"))
def prime_num(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
            print("Prime number")
    else:
        print("Not a prime number")
prime_num(num)