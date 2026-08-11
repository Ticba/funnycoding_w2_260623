# ASCII Code


# 字.join(List)     # '*'.join(['1', '2', '3']) -> '1*2*3'



# 1. 輸入 COD          
s_input = input()


# 2. 先產生 ['67', '79', '68']
# 2.0 先生成一個空的 List
ans_list = []

# 2.1 迴圈處理每一個字元
# 例： 'C' -> 67, 'O' -> 79, 'D' -> 68
for c in s_input:
    ascii_c = ord(c)  # 轉換成 ascii code 編號


# 2.2 把轉換過後的數字（編號）加入 List 
# list名稱.append(data)
    ans_list.append(str(ascii_c))   # 字串版本的 ascii code 存入 ans_list 


# 把 data 加入 List

# 3. '_'.join(['67', '79, '68']) -> '67_79_68'
#  補充： .join(list) 的這個 list 他要全部由 str 元素組合成
print('_'.join(ans_list))