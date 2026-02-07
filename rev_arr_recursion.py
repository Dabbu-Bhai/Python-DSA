arr = [1,2,3,4,5,6,7,8,9]
left = 0
right = len(arr)-1

def rev(arr,left,right):
    if(left==right):
        return 0
    arr[left],arr[right] = arr[right],arr[left]
    rev(arr,left+1,right-1)
rev(arr,left,right)
print(arr)