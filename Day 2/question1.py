"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),
..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
Example 1:
Input: nums = [1,4,3,2]
Output: 4

"""

def MinSums(lst):
    lst.sort()
    #Once numbers are sorted, the sum of min(an,bn) will be the sum of all odd elements
    result = 0
    numslen = len(lst)
    #Adding all odd elements into result
    for i in range(0, numslen-1, 2):
        result += lst[i]
    print(result)


lst=[]
nums = int(input("enter number of elements "))

if nums % 2 != 0:
    print("please enter an even")
else:
    for i in range(0, nums):
        ele = int(input())
        lst.append(ele)


MinSums(lst)


"""
INPUT
enter number of elements 6
1
2
3
4
5
6

OUTPUT 
9   (1+3+5 - sum of all odd elements)
"""