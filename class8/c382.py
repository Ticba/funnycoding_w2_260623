# 12+3


s = input() # '12+34'

first_n = ''
second_n = ''

for c in s:
    if c in '0123456789':
        second_n += c           # 不管要存第一個數字或第二個數字都暫放在 second_n
    else:
        first_n = int(second_n) # 當遇到 op 把 first_n 設定成 second_n 暫存的內容並清空 second_n
        second_n = ''
        op = c
second_n = int(second_n)

# 12 '+' 34


if op == '+':
    print(first_n + second_n)
elif op == '-':
    print(first_n - second_n)
elif op == '/':
    print(first_n // second_n)
else:
    print(first_n * second_n)
# 15