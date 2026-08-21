# 流程

# 1. 程式由上而下一行一行執行

# 2. 分岔： if-elif-else

# 3. 重複： 迴圈 for , while

# 4. 分離（打包）一些功能出來另外寫


import random

def my_calculate(number):   # 定義函式 (define function)
    # 這塊程式執行的內容
    # 預先開好 number 變數空間，等待使用時指定的值
    print(a / number + (number-1) * b / number)
    


for _ in range(5):
    # 隨機生成兩個數字 a, b
    # 輸出 1/3 * a + 2/3 * b 的結果
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    # print(a / 3 + 2 * b / 3)
    my_calculate(3)   # 呼叫函式 (call function)   

    # 輸出 1/4 * a + 3/4 * b 的結果
    # print(a / 4 + 3 * b / 4)
    my_calculate(4)

    # 輸出 1/5 * a + 4/5 * b 的結果
    # print(a / 5 + 4 * b / 5)
    my_calculate(5)


    # print(), input(), len()
    # 可以自己定義自己想用的功能 -> 計算 1/n 倍 a + (1 - 1/n) 倍 b
    # 取名 my_calculate()



# 自定義函式

# 基本版
'''syntax
def 函式名稱():
    # 函式執行的程式碼（要縮排）
    # 第一行函式
    # ....
    # 最後一行函式

某某指令    # 不是函式的內容


'''

# 有參數&回傳值的版本
'''syntax 語法
def 函式名稱(參數名稱1, [參數名稱2...]):        -> 參數之間以「逗號」區隔
    # 函式執行的程式碼（要縮排）
    # 第一行函式
    # ....
    # 最後一行函式
    # return 回傳的資料         (只要執行到 return 敘述，return 就式函式裡的最後一個指令)

某某指令    # 不是函式的內容
'''


# 定義自己的加法函式 - 想要設計一個把五個數字加在一起的函式

def add_5(n1, n2, n3, n4, n5):
    s = n1 + n2 + n3 + n4 + n5
    return s
    


# 預期的效果
a = add_5(1, 2, 3, 4, 5)    # 輸出 15
b = add_5(1, 2, 3, 4, 4)    # 輸出 14
c = add_5(1, 2, 3, 2, 1)    # 輸出 9

print(a, b, c)              # 先把回傳值存起來，再輸出
print(add_5(1, 0, 0, 0, 0)) # 輸出 add_5(1, 0, 0, 0, 0) 的回傳值


3 x
4 o
5 x

...

25 o