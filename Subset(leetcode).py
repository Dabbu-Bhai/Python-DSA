# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

from typing import List
nums = [1,2,3]
def subsets(nums: List[int]) -> List[List[int]]:
    result = [] #storing result

#Creatting a recursive function that takes the index and an empty list as its parameters ans runs recursively to find all the possible combinations/subsets
    def subset(index : int,current: List[int]):

        #base condition is if index == len(nums) then we append our current subset to result and return
        if(index == len(nums)):
            result.append(current[:])
            return
        
        #now we include our first choice
        current.append(nums[index])
        subset(index+1 , current)

        #backtrack and remove last element
        current.pop()

        #exclude the first option now
        subset(index+1,current)

  
    subset(0,[])    
    return result

print(subsets(nums))
