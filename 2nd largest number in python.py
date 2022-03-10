list = []
arr = [7,2,2,4,1,7,8,8]
arr.sort(reverse=True)
print(arr)
#print(arr[-2])
for i in range(len(arr)-1): 
     if arr[i] <= arr[i+1]:
            list.append(arr[i+1])
list.sort()            
print(list)
print(list[-2])