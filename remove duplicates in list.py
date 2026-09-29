A=[1,3,5,2,3,1,5,6,4,7,6,8,9,8]
B=[]
for elem in A:
    if elem not in B:
        B.append(elem)
print(B)