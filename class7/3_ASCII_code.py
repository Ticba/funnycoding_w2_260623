'A' 
'B'
'C'
'a'
'1'
' '
'!'

# 字元 -> ASCII 編碼

print(ord('A'))     # 65
print(ord('a'))     # 97

print(ord('A') - ord('T')) # A 跟 T 差了 19 個符號

# 字元 <- ASCII 編碼    # character
print(chr(65))      # 'A'


'apple' 

'加密 & 解密 shift value'

# string 也是可迭代的物件，迭代的方式為一次一個字元
ans = ''
for c in 'apple':
    ans += chr(ord(c) + 1)  # loop1: a -> 97 -> 98 -> b

print(ans)

origin = ''
for c in ans:
    origin += chr(ord(c) - 1)  # loop1: b -> 98 -> 97 -> a

print(origin)


# f035

# CODEWARS
# 
s = input()
ans = ''
for c in s:
    ans += str(ord(c))

print(ans)