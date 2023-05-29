"""
    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

    **Example 1:**
    Input: nums = [1,2,2,4]
    Output: [2,3]

"""


def ErrorNumbers(nums):
        #taking the length of the list and assigning number of duplicates as 0 initially
        N, dupe = len(nums), 0
        #assigning list of 0 equal to length of list plus one [0,0,0,0,0], and expected Sum of the list if all numbers are present in order with no missing numbers
        seen, sumN = [0] * (N+1), N * (N+1) // 2
       
        #iterating each number and subtracting from Sum, the first number is 1 , so SumN will be 10-1 = 9
        for num in nums:
            sumN -= num
            #if the index equivalent of the number is a positive number in the empty array, assign that number to the duplicate variable,
            #the first number is 1, 
            if seen[num]: 
                dupe = num    
            #the first number is 1, so index 1 of the empty array is assigned 1,
            #in next iteration number is 2, so index 2 of empty array will be assigned 1,
            #in next iteration number is 2 again, so infex 2 of empty array will contain 1+1 =2
            seen[num] += 1
        return [dupe, sumN + dupe]

nums = [1,2,2,4]

print("answer is",ErrorNumbers(nums))


"""INPUT
nums = [1,2,2,4]

OUTPUT
answer is [2, 3]
"""