list_binary=[1,2,3,4,5,6,7,8,9]
search=8
def binary_search(list_binary,search):
    low=0
    high=len(list_binary)-1
    while low<=high:
        mid=(low+high)//2
        if list_binary[mid]==search:
            return mid
        elif list_binary[mid]>search:
            high=mid-1
        else:
            low=mid+1
    return -1
result=binary_search(list_binary,search)
print("Founded at:",result)