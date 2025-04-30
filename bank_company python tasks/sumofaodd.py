number=input("Enter any numbers:")
odd_sum=0
for i in number:
    if int(i)%2!=0:
       odd_sum+=int(i)
print("The odd sum is:",odd_sum)