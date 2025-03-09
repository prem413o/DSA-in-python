def linear_search(arr,target):
    size=len(arr)
    
    for index in range(0,size):
        if(arr[index]==target):
            return index
        
    return -1



num=[10,15,14,85,45,63]

target=int(input("Enter your number: "))

result=linear_search(num,target)

print(result)