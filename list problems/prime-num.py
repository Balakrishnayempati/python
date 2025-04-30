list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
def prime(inp):
    count=0
    for i in range(1,inp+1):
        if inp%i==0:
            count+=1
    if count==2:
        print("Prime number",inp)
    else:
        print("Not a prime",inp)

for i in list:
    prime(i)