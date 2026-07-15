# 變數 variable
# 1 存資料的空間
# 2 存一筆資料

# 變數的概念（ipad 畫畫）

# 箱子
# a. 名稱自己取
# b. 不能與其他變數名稱相同

aVariable = 10
bVariable = 20

print(aVariable, bVariable)

aVariable = 30  # override 覆蓋掉原本的值
print(aVariable, bVariable)

# c. 名稱開頭不能是數字

# d. 大小寫視為是不一樣的字
AVariable = 40
print(aVariable, bVariable, AVariable)

# 找變數用 cmd + f

# 3 Num (int, float), String, Boolean

# Boolean

aBoolean = True
cBoolean = False
dBoolean = (3 > 0)  # 對 True
eBoolean = (3 < 0)  # 錯 False

print(aBoolean, cBoolean, dBoolean, eBoolean)

# 程式為什麼需要儲存對或錯？
# 程式可以依據不同的情況做不同的事情

# 假設機器人遇到分叉路
# fBoolean = (前面有沒有障礙物)  
# True  -> 右轉
# False -> 繼續直走 


# type(資料) -> 資料類型

print(type(1))      # int
print(type(1.0))    # float
print(type("a"))    # str
print(type(True))   # bool

a, b, c, d = 4, 4.0, "banana", 3 < 0
print(type(a))
print(type(b))
print(type(c))
print(type(d))
