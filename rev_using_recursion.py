# arr = [1,2,3,4,5,6,7,8,9]
# left = 0
# right = len(arr)-1

# def rev(arr,left,right):
#     if(left==right):
#         return 0
#     arr[left],arr[right] = arr[right],arr[left]
#     rev(arr,left+1,right-1)
# rev(arr,left,right)
# print(arr)

# def isPalindrome(s):
#         # code here
#         x=list(s)
#         # print(x)
#         l = 0
#         r = len(x)-1
#         def helper(x,l,r):
#             if(l >= r):
#                 return x
#             x[l],x[r] = x[r],x[l]
#             helper(x,l+1,r-1)
#         helper(x,l,r)
#         x = "".join(x)
#         print(x)
#         if(x==s):
#             return True
#         else:
#             return False

# s="abba"
# x = isPalindrome(s)
# print(x)