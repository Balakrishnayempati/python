for i in range(n):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(n):
        if i==j or i==n-1 or j==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
    
    n=7
for i in range(n):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(n):
        if i>=j:
            print("*",end=' ')
        # else:
        #     print(" ",end=' ')
    print()



n=7
num1,num2=0,1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(num1,end=' ')
            num1,num2=num2,num1+num2
    print()



n=5
track1=False
for i in range(n):
    start=i+1
    for k in range(2*(n-i-1)):
        print(' ',end='')
    for j in range(2*i+1):
        print(start,end=' ')
        start-=1
    print()

n=5
track1=False
for i in range(n):
    start=i+1
    for k in range(2*(n-i-1)):
        print(' ',end='')
    for j in range(2*i+1):
        print(start,end=' ')
        if start==1:
            track1=True
        if track1 == False:
            start-=1
        else:
            start+=1
    print()

n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print('*',end='')
    print()