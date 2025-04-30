list=[9474,145,153,2424]

def check_armstrong(inp):
    num=inp
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit** len(str(num))
        temp=temp//10
    if sum ==num:
        print(num,"Armstrong")
    else:
        print(num,"Not an armstrong number")

for i in list:
    check_armstrong(i)
