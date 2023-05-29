"""
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    **Example 1:**
    Input: nums = [1,2,3,1]

    Output: true
"""



def returnCount(i):
    #Setting a Flag assuming all values are unique
    global count
    if i in dict1:
        dict1[i] += 1
        count += 1
    else:
        dict1.update({i: 1})
    

nums = [1,2,5,65,323]
dict1 = {}
count=0

    

for i in nums:
    returnCount(i)

for key,value in dict1.items():
    if value >= 2:
        print("the key ", key," appears ", value , " number of times")


if count > 0:
    print("Elements are repeating")

else:
    print("All elements are unique")


"""
INPUT 
nums = [1,2,5,65,323]

OUTPUT
All elements are unique
"""

