def Binary_search(arr,target):
  left =0
  right=len(arr)-1
  while left<=right:
    mid = int((left+right)/2)
    if arr[mid] == target :
      return mid
    elif arr[mid]>target:
      right = mid-1
    else :
      left = mid+1
  
  return -1

sorted_arr = list(map(int,input("Enter a sorted array (space-seperated) : ").split()))
target = int(input("Enter the target element to search for : "))

result = Binary_search(sorted_arr,target)

if result != -1 :
  print("Element found at index : ",result)
else :
  print("Element not found")
