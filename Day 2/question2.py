"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started
to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice
likes her candies very much, and she wants to eat the maximum number of different types of
candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types
of candies she can eat if she only eats n / 2 of them.
Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one
of each type
"""

def getUnique(i):
    if i in dict1:
        dict1[i] += 1
    else:
        dict1.update({i:1})



candyType=[1,1,5,5,4,4,1,1,9,9]
dict1={}
if len(candyType)%2 != 0:
    print("Number of candies is odd")
else:
    print("number of candies is", len(candyType))


for i in candyType:
    getUnique(i)

print(dict1)
if len(dict1)/2 <= len(candyType)/2:
    print("number of candies Alice can have that includes one unique candie of each type is", len(dict1))



"""
INPUT
candyType=[1,1,5,5,4,4,1,1,9,9]
OUTPUT
number of candies is 10
{1: 4, 5: 2, 4: 2, 9: 2}
number of candies Alice can have that includes one unique candie of each type is 4
"""