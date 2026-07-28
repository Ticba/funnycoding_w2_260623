# h m
# 6 00 x
# 6 30 x
# 7 00 x
# 7 30 o
# 8 00 o


# ..

# 16 00 o
# 16 30 o
# 17 00 x

# 7 30  以前不在
# 17 00 以後（含）不在

# 用 h m 來判斷

h, m = input().split(' ') # h = '17' m = '00'
h = int(h)
m = int(m)
# if h == 7 and m < 30: ( h <= 7 且 m < 30)
#   不在
# elif h < 7:
#   不在
# elif h >= 17:
#   不在
# else:
#   在
