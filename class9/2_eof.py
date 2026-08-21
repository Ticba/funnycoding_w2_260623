# End of File 的判斷 (EOF)

# 解題系統的輸入其實可以想成一個檔案，結尾都有包含一個 EOF 符號


while True:
    try:
        input() # input() 如果想要讀取 EOF 就會產生 error
    except:
        break