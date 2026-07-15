# 輸出技巧
# str.join(list) -> 利用字串1去連接 list 裡面的所有東西

# pre_stuff.method_name(other_stuff)

# 使用情境：輸入有很多，不確定有幾個

# 例子：apple banana pineapple guava


fruits_list = input().split()
print(fruits_list)


# 題目要求：連接後輸出，連接的字 "*"
# apple*banana*pineapple*guava

# print("*".join(fruits_list))
print("\t".join(fruits_list))

# ---------特殊的字---------

'\n'
'\t'    # 4 格或 8 格（對應到 tab）