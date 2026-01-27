# #extract number of digits
# num = int(input("Enter number : "))
# temp = num
# while(temp>0):
#     print("digit is : ",temp % 10)
#     temp = temp // 10

# #Count number of Digits
# num = int(input("Enter number : "))
# temp = num
# count = 0
# while(temp>0):
#     count+=1
#     temp = temp // 10
# print(count)

# # CHECK IF NUMBER IS PALINDROME OR NOT
# num = int(input("Enter number : "))
# temp = num
# rev = 0
# while(temp>0):
#     rev = rev*10 + temp % 10
#     temp = temp // 10
# if rev == num:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# # # ARMSTRONG NUMBER
# num = 153
# temp = str(num)
# pow = len(temp)
# # print(pow)
# arm=0
# temp = num
# digipow = 0
# # print (temp)
# while(temp>0):
#     digipow = (temp % 10) ** pow
# # print(digipow)
#     arm = (arm) + digipow
#     # print(arm)
#     temp = temp // 10
# # print(arm)
# if arm == num:
#     print("Number is Armstrong number")
# else:
#     print("Number is not Armstrong number")

# # ALL FACTORS OF A GIVEN NUMBER
# num = 24
# fact= []
# for i in range (1,(num//2)+1):
#     if(num % i == 0):
#         fact.append(i)
# fact.append(num)
# print(fact)

# STORE FREQUENCY IN DICTIONARY 
# nums = [1,1,1,2,2,3,3,4,5,6,6,6,6]
# hash_map = {}
# for i in range(0,len(nums)):
#     hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
# print(hash_map)