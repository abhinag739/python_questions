array1 = [1,2,3,4,5,5,6]

N = len(array1)


for  i in range(0,len(array1)-1):
    for j in (i+1 , len(array1)-1):
        if(array1[i] == array1[j]):
            print(array1[j])

