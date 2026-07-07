# 1
# 2
# 4
# 9
# 10
# 請相加

# 分成五行給你輸入
# input() 就是讀一整行

"""n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

print(n1 + n2 + n3 + n4 + n5)"""


# 給的格式不同怎麼辦？

# 1 2 4 9 10

n_L = input().split() # '1 2 4 9 10'.split() 以空格拆成 list => ['1', '2', '4', '9', '10']
print(n_L)
print(int(n_L[0])+int(n_L[1])+int(n_L[2])+int(n_L[3])+int(n_L[4]))