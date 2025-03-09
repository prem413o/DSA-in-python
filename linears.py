#linear search in a list,target

num=[10,23,45,50,60]

target=int(input("Enter your number for finding: "))
i=0

while i<len(num):
    if(target==num[i]):
        print("found at index",i)
        break
    else:
        print("not found")
    i+=1