# 取用 list 或是 string 裡面的 item/element 元素

# list 
a_list = [1, 3, 5, 7, 9]    # 編號： 0(-5) ~ 4(-1)

# ----->  |

# 取單一 item
x = 0
a_list[x]

y = -1
a_list[y]

# slicing (蛋糕取其中一部份)
print(a_list[0:3:1])        # [1, 3, 5]    取從 0 開始，到 3 停止，每次間隔為 1。

# a_list[start:stop:step]   start: 開始（會取）。stop: 結束（不取）。step: 間隔。

print(a_list[3:1:-1])       # [7, 5]




# 預測題：
"""
a_list[0:-1:1]      # [1, 3, 5, 7]
a_list[-1:0:-1]     # [9, 7, 5, 3]
a_list[0:3:-1]      # []
a_list[3:0:1]       # []

"""
print(a_list[0:-1:1])           # [1, 3, 5, 7]
print(a_list[-1:0:-1])          # [9, 7, 5, 3]
print(a_list[0:3:-1])           # []
print(a_list[3:0:1])            # []


"""
a_list[0:4:2]       # 
a_list[0:1:2]       # 
a_list[-1:-4:-3]    # 
a_list[-2:-5:-2]    # 

"""

print(a_list[0:4:2])       # 
print(a_list[0:1:2])       # 
print(a_list[-1:-4:-3])    # 
print(a_list[-2:-5:-2])    # 



# length     len(多元素結構)       ->      結構有幾個元素
print("取長度用 len:", len(a_list))

first = a_list[0]                   # 取第 0 個
left = a_list[1:len(a_list):1]      # 從第 1 個取到最後一個

print(first, left)


