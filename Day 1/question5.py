"""
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 

    nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
    
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    **Example 1:**
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

"""

test_list1 = [1, 5, 0, 0, 0, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
 


res = sorted(test_list1+test_list2)
res1 = [i for i in res if i != 0]

print("the sorted result with the zeros is", res)
print("the sorted result ignoring the zeros is", res1)


"""
INPUT 
test_list1 = [1, 5, 0, 0, 0, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
 

OUTPUT
test_list1 = [1, 5, 0, 0, 0, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
 
"""