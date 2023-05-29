#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twosum(nums, target) -> int:
    i=0
    list1=[]
    for i in range(len(nums)-1):
        for j in range (len(nums)):
          if (nums[i] + nums[j]) == target[0]:
            list1.append([i,j])

    return(list1)
        

 
nums = [2,1,5,3,7,0,1]
target = [8]
print("the indices  which add up to match the target value", target[0], " are ", twosum(nums,target))
