# for 迴圈
# 元素個數
# iterate （更）迭代（換），代換到前面寫的變數

''' 參考用
for i in [1, 2, 3, 4]:  # 元素個數：4
    print(i)    # loop1: i = 1 , loop2: i = 2, loop3: i = 3, loop4: i = 4

'''

# syntax

'''
for 變數名稱 in 可迭代的多元素物件:
    重複執行的程式區塊

'''

for i in range(1, 5, 1):    # loop1: i = 1 , loop2: i = 2, loop3: i = 3, loop4: i = 4 
    print(i)

# range()  快速建立多個數字

# 1
# range(start, stop, step)    # start 開始建立，stop 停下來（不包含），step 是每次步伐

# 2
# range(start, stop), step = 1

# 3
# range(stop)   , start=0, step=1

for i in range(101):
    print(i)    # 0, 1, 2, 3, 4


# c419

"""n=int(input())

for i in range(1, n+1):
    print("_"*(n-i) + "*"*i)"""


# 兩種迴圈使用上的差異
# 1. while 
# 適合用條件決定什麼時候要停止重複
# 可能次數會不一定

# 2. for
#    a.適合知道要重複的次數
#    b.適合知道要迭代的物件



# a.
for _ in range(100):
    print('hello')

# b.
# a = input.split()
# 舉例：處理完之後，拿到 [5, 3, 4, 2, 7, -1, 8, 100, 6]

inputList = [5, 3, 4, 2, 7, -1, 8, 100, 6]
for n in inputList:
    print(n+2)

# c. 你希望迴圈運作的時候要保有 idx 資訊
# 題目希望你找找看某個數字(target)有沒有在 list 之中
# 請告訴我們他在第幾個

# input:
'''
5
3 7 9 10 ... -2 5
'''
print('----------')
target = 5
inputList = [3, 7, 9, 10, -2, 3 ,1, 2, 5]

for idx in range(len(inputList)):
    # idx 0~5
    n = inputList[idx]
    if n == target:
        print(idx)
