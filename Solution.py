import numpy


inp = input().split(" ")

n = int(inp[0])
m = int(inp[1])
temp = []

for x in range(n):
    row = input().split(" ")
    for y in range(m):
        row[y] = float(row[y])
    temp.append(row)
 
#mean 1
#var 0
#std None

temp = numpy.array(temp)

print(numpy.mean(temp,axis=1))
print(numpy.var(temp,axis=0))
std = str(numpy.std(temp,axis=None))

if len(std) >12:
    string = std[0:12]
    last = int(std[12:13]) + 1

    print(string+str(last))
else:
    print(std)
