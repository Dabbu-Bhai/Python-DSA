def selectionsortasc (nums : list[int]):
    n = len(nums)
    for  i in range(n):
        min_ind = i
        for j in range (i+1,n):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[min_ind], nums[i] = nums[i] , nums[min_ind]

def selectionsortdsc (nums : list[int]):
    n = len(nums)
    for  i in range(n):
        max_ind = i
        for j in range (i+1,n):
            if nums[j] > nums[max_ind]:
                max_ind = j
        nums[max_ind], nums[i] = nums[i] , nums[max_ind]

def bubblesortasc(nums: list[int]):
    n = len(nums)
    is_swap = False
    for i in range (n-2,-1,-1):
        print(nums)
        for j in range(0,i+1):
            if(nums[j] > nums[j+1]):
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                is_swap = True
        if is_swap == False:
            break

def bubblesortdsc(nums: list[int]):
    n = len(nums)
    is_swap = False
    for i in range (n-2,-1,-1):
        # print(nums)
        for j in range(0,i+1):
            if(nums[j] > nums[j+1]):
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                is_swap = True
        if is_swap == False:
            break


nums = [5,7,8,4,1,6,9,2,3]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# selectionsortasc(nums)
# selectionsortdsc(nums)

# bubblesortasc(nums)
# bubblesortasc(nums2)
# print("")
# bubblesortdsc(nums)

# print(nums)

