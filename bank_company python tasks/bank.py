print("Give a perfect ac number")
num=int(input("Enter any number:"))
sum=0
for i in range(1,num):
    if num%i==0:
     
     print(i)
     sum+=i  
if sum==num:
       print(num,"is perfect number")
else:
       print(num,"is not a perfect number")
      
    