num=10
total=0
for i in range(0,num+1):
  if i%2==0:
     total+=i*100
     print("The even numbers:",i*100)
  else:
   print("The odd numbers:",i)
print("The total finance is:",total)