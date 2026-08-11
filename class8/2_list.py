# List [] (Sequence 的一種)

# 可以收集多筆資料的一種儲存形式（資料結構）
# 1. 順序性

[1, 3, 5, 6, 7] # 1 是 0 號，3 是 1 號 ...
[1, 3, 5, 7, 6] # 是另一個 list


# 2. 每筆資料都沒有名稱（是以編號來取用）


# A. 建立 List

變數名稱 = []
變數名稱 = list()   # 類似使用一個 function 來建立 list

print(list((1, 2, 3)))

# B. 取用 List 元素
# 請參考 class5/1_indexing.py & class7/1_indexing2.py


# C. 新增元素
# 1. list名稱.append(元素)    => 加入到最後
aList = [3, 5, 7]
aList.append(20) # [3, 5, 7, 20]
print(aList)        # 檢查修改完的結果


# 2. list名稱.insert(編號, 元素)
aList = [3, 5, 7]
aList.insert(1, 20) # [3, 20, 5, 7]
print(aList)        # 檢查修改完的結果


print('------------')
# D. 刪除元素
del aList[2]        # [3, 20, 7]
#del aList[100]     # list out of range
print(aList)

aList.remove(3)     # [3, 20]
print(aList)

# E. 修改內容
a = 1
a = 2

aList = [0,1,2,3,4,5,6]
aList[3] = 20   # [0,1,2,20,4,5,6]
print(aList)


# F. 查看 List 元素的個數
print(len([3, 5, 6]))
