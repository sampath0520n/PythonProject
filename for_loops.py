#for loop example
a=[10,20,30,40]
sum=0
for i in a:
    sum=sum+i
print(sum)
#nested loops
for m in range(4):
    for n in range(3):
        print(f"({m},{n})")