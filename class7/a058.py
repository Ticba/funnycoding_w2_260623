# 第一行輸入：代表的是接下來出現的數字個數

# 提示：開票正字記號

n = int(input())

count3k = count3k1 = count3k2 = 0

for _ in range(n):
    # 總共會重複 n 次
    # 1. 你需要 input()，然後除以 3 看餘數
    number = int(input())
    r = number % 3  # r=0, 1, 2
    # 2. 看是哪一組，就讓那個變數 +1
    if r==0:
        count3k += 1
    elif r==1:
        count3k1 += 1
    else:
        count3k2 += 1

print(count3k, count3k1, count3k2)