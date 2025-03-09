#Binary search

def Binary_search(num,target):
    size=len(num)

    start=0
    end=size-1
    

    while(start<=end):
        mid=(start + end)//2

        if(num[mid]==target):
            return mid #found the target
        
        elif(num[mid]>target):
            end=mid-1
        elif(num[mid]<target):
            start=mid+1

    return -1


num=[10,20,35,45,55,70,85]
target=int(input("Enter your number: "))

result=Binary_search(num,target)
print(result)