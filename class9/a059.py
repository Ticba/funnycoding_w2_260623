# sample input:
'''
2
1
5
5
35
'''

# sample output:
'''
Case 1: 5
Case 2: 50
'''

def saps(n1, n2):
    ans = 0
    for n in range(n1, n2+1):
        '''1*1 != 9
        2*2 != 9
        3*3 == 9 (V)

        1*1 != 8
        2*2 != 8
        3*3 > 8'''
        check = 1
        while check*check <= n:
            if check*check == n:
                # n 是完全平方數
                ans += n
            check += 1

    return ans
        



t = int(input())

i = 1
while True:      # i 範圍 0~(t-1)
    try:
        # 每一次處理一筆測資
        a = int(input())
        b = int(input())
        ans = saps(a, b) # sum_all_perfect_square
        print("Case ", i, ": ", ans, sep='')
        i += 1
    except:
        break

