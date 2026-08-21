s=input()
length = len(s)
# 1
pre = 0         # 把想要追蹤的狀態存成變數：前面的編號
next = 1        # 把想要追蹤的狀態存成變數：後面的編號
for _ in range(length-1):
    # 要重複做的事（縮排）
    a=ord(s[pre])-ord(s[next])   # 編號處理
    if a<0:
        a=-a
    print(a,end='')

    pre += 1
    next += 1

# 接著要改成可以解 10 ~ 20 大寫英文字母

# # 2
# b=ord(s[1])-ord(s[2])
# if b<0:
#     b=-b
# print(b,end='')
# # 3
# c=ord(s[2])-ord(s[3])
# if c<0:
#     c=-c
# print(c,end='')
# # 4
# d=ord(s[3])-ord(s[4])
# if d<0:
#     d=-d
# print(d,end='')
# # 5
# e=ord(s[4])-ord(s[5])
# if e<0:
#     e=-e
# print(e,end='')
# # 6
# f=ord(s[5])-ord(s[6])
# if f<0:
#     f=-f
# print(f,end='')

# 不一樣的部分
print()