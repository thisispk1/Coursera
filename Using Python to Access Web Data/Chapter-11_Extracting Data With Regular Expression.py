import re
f = open('Ass_11 regex_sum.txt')
numList = []
for lines in f:
    num = re.findall('[0-9]+',lines)
    numList = numList + num
#print(numList)
numsum = 0
for i in numList:
    i = float(i)
    numsum = numsum + i
print(int(numsum))
