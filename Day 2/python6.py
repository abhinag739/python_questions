#input 2 10
#output 2 4 6 8 10  (all multiples of either 2 or 5)


input1 = 2
input2 = 10
res=[]
for i in range(2,10+1):
    if i%2 == 0 or i%5 ==0:
        res.append(i)


print(res)