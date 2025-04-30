input=int(input("Enter any number:"))
def prime_number(input):
    count=0
    for i in range(1,input+1):
        if input%i==0:
         count+=1
    if count==2:
            return 'Prime number'
    return 'Not a prime number'
print(prime_number(input))
