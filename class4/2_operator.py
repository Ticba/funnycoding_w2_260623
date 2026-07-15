# operator 運算子
# ：作用於運算元


# 數學
"""
operator 運算子
+ , -, x 

operand 運算元
1, 2
"""

#  1 + 1
# 元 子 元

# 看到上面，我們就知道要做加法，加 1 & 1


# 1 @ 1 -> 前 x 5 - 2 + 後



# python 程式

'用使用方式來分類'
# 二元運算子
# +, -, *, **, /, //, %
# 使用方式： 元 子 元

# 一元運算子
# -
# 使用方式： 子 元

-5


'用功能來分類'

# 1. 算數運算子
# +, -, *, **, /, //, %



# 2. 指定運算子
# =
var = 1
var_2 = 3*5/2


# "=" 使用方式
# 左變數 = 右運算結果
# 意義是將「運算結果」存入/指定「變數」

# 3. 比較運算子
# 結果都是 bool
# >, <, >=, <=
# 左是否「等於」右 -> ==
# 左是否「不等於」右 -> !=

3 > 0   # True
5 >= 5  # True
5 == 5  # True
3 == 7  # False
3 != 7  # True


# 4. 邏輯運算子
# 使用方式： 元 子 元   /   子 元
# 元：限定在 bool
# and, or, not

# 考一百分 and 念書40小時以上
print(True and True)     # True     有考一百，且有念 40 小時以上
print(True and False)    # False    有考一百，但沒有念 40 小時以上
print(False and True)    # False    沒考一百，但有念 40 小時以上
print(False and False)   # False    都沒有


# 考一百分 or 念書40小時以上
print(True or True)     # True     有考一百，且有念 40 小時以上
print(True or False)    # True     有考一百，但沒有念 40 小時以上
print(False or True)    # True     沒考一百，但有念 40 小時以上
print(False or False)   # False    都沒有


# not True -> False, not False -> True

# 「沒有」考一百分？
print(not True)     # False
print(not False)    # True
