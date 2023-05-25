def count(i):
    if i in dict1:
        dict1[i] += 1
    else:
        dict1.update({i: 1})




array1 = [3,4,3,2,3]

dict1={}

for i in array1:
    count(i)


for key, value in dict1.items():
    if value >= len(array1)/2:
        print("the key whose length is over half the total length of the array is ", key," number of times it occurs is", value)