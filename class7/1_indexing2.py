# 簡化版 slicing
# aList[start:stop:step]

aList = [1,3,5,7,9,11]
# 1. aList[1:5]     aList[start:stop] ,step = 1

print(aList[1:5])   # [3, 5, 7, 9]

print(aList[5:1])   # []

# 2. aList[1:]      aList[1:len(aList)], step = 1
#    aList[:3]      aList[0:3], step = 1

print(aList[1:])    # [3, 5, 7, 9, 11]
print(aList[:3])    # [1, 3, 5]



# 3. aList[::]
print(aList[::])    # aList[0:len(aList):1]

# 練習
aList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bList = aList[:5]
cList = aList[5:]

dList = bList[3:1:-1]
eList = cList[4::-2][1]

print(bList)    # [0, 1, 2, 3, 4]
print(cList)    # [5, 6, 7, 8, 9, 10]
print(dList)    # [3, 2]
print(eList)    # 7     先想 cList[4::-2] 是 [9, 7, 5] 再想 cList[4::-2][1] -> [9, 7, 5][1]