# Sequence process

# 濕搓沖捧擦
# (1) 濕
# (2) 搓
# ....

# 程式由上往下執行
# 快(看到) -> 慢(思考)


# branch process 分支

# 打球？
# 查詢氣象預報，讀取降雨機率 x %
# 如果 x > 50 ，那就不打球
# 如果 x <= 50，那就出去打球

# x = 20

# if x > 50:      # if 條件
#     print("去打球")     # 當 x > 50 是對的條件，會執行這裡。
#     print("True")
# else:           # else
#     print("待在家")     # 當 x > 50 是錯的條件，會執行這裡。    
#     print("False")
# print("if-else 都判斷完的程式")



## 只有 if 沒有 else 的一個例子
# 輸出角度
# 如果是廣義角，要先化簡

x = -20
if x > 360 or x < 0:
    x %= 360
print(x)


## if-elif-else 的例子

age = 70 
# age > 65: 敬老 , age 0 ~ 18: 學生, else: 全票

if age > 65:
    print("敬老")
elif age <= 18 and age >= 0:
    print("學生")
elif age > 18 and age <= 30:
    print("壯年")
else:
    print("中年")



# 常見的判斷式
# a 除以 b 有沒有整除

5 % 3 # 2
3 % 3 # 0 整除就是餘數為零