num=134
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
print(sum)
