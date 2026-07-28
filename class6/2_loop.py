# 重複執行 loop


# 輸出 1 ~ 100，每一個數字一行

print(1)    # 0 + 1
print(2)    # 1 + 1
print(3)    # 2 + 1
print(4)    # 3 + 1
print(5)    # 4 + 1
print(6)    # 5 + 1

print('------------')

# 先試著重複輸出 1 ，總共輸出 6 行

"""
while 條件:
    要重複做的事情

1. 檢查條件
2. 條件為 True，執行重複的事情

"""
count = 0       # count 是一個變數
while count < 6:
    # 要重複做的事（縮排）
    print(1)

    # count + 1
    count += 1
    print("裡面的程式")
print("外面的程式")

"""
展開來其實是：
1. count = 0
2. 判斷 count < 6 是不是 True
3. print(1)
4. count += 1   ->  count 是 1
(重複)
5. 判斷 count < 6 是不是 True
6. print(1)
7. count += 1   ->  count 是 2
(重複)
8. 判斷 count < 6 是不是 True
9. print(1)
10. count += 1   ->  count 是 3
(重複)
11. 判斷 count < 6 是不是 True
12. print(1)
13. count += 1   ->  count 是 4
(重複)
14. 判斷 count < 6 是不是 True
15. print(1)
16. count += 1   ->  count 是 5
(重複)
17. 判斷 count < 6 是不是 True
18. print(1)
19. count += 1   ->  count 是 6
(重複)
20. 判斷 count < 6 是 Fasle
"""

# 先試著重複輸出一個愈來愈大的數字 (1~6) ，總共輸出 6 行

count = 1
while count <= 6:
    print(count)
    count += 1


# 先試著重複輸出一個愈來愈大的數字 (1~100) ，總共輸出 100 行

count = 1
while count <= 100:
    print(count)
    count += 1




# (n1, n2)
# (1, 1)
# (2, 3)
# (3, 5)
# (4, 7)



# (100, )

# n1 每重複一次 +1
# n2 每重複一次 +2


count = 1
n1 = 1
n2 = 1
while count <= 100:
    # (todo)
    print("(",n1, ", ", n2, ")", sep='')
    n1 += 1
    n2 += 2
    # (end)
    count += 1


# c418

# 輸入範例
# 3

# 輸出範例
# *     (star: 1)
# **    (star: 2)
# ***   (star: 3)

"""aInput = int(input())   # 讀數字轉換成 int 類型

count = 1               # count 專門控制迴圈重複
n = 1                   # n 處理跟題目相關的邏輯
while count <= aInput:
    print('*' * n)
    n += 1
    # 邏輯處理完
    count += 1"""

# c419
"""
____*
___**
__***
_****
*****
"""

print("_"*n1 + "*"*n2)


# c420
"""
___*___     #  3     1     3   代表 「底線 星星 底線」 的數量
__***__     #  2(-1) 3(+2) 2(-1)   
_*****_
*******
"""




# b877

# input: 5 10, output: 5
# input: 99 5, output: 6
# 99 -> 0 -> 1 -> 2 -> 3 -> 4 -> 5

start, end = input().split(' ')
start, end = int(start), int(end)

# times = 0   # 紀錄次數的變數
# while start != end: # 5 != 5
#     times += 1
#     start += 1
#     if start == 100:
#         start = 0

# print(times)


# 2
# if end >= start:
#     print(end-start)
# else:
#     print(end+100-start)

# 3
# print((end+100-start) % 100)
