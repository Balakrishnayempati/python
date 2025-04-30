

def sum(a,b,*args):
    sum=0
    print("a =",a)
    print("b =",b)
    print(args) #it prints in tuple and it has only *
    print("Even number are:")
    for i in args:
        if i%2==0:
            print(i)
            sum+=i
    return sum

print(sum(2,1,2,3,4,5,6,7,8,9,10,11,12))
            
        
        