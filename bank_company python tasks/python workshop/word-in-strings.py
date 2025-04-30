word=str(input("Enter any words:"))
count=1
space=" "
for i in word:
    if i==space:
        count+=1
print(count)