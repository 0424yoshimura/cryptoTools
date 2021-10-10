#The program outputs all the patterns of the shifting numbers of the Caesar cipher.

plainText = ""
result = ""

print("Enter plain text.")
plainText = input()

for i in range(1,26):
    for c in plainText:
        if ord('a') <= ord(c) <= ord('z'): #小文字の変換
            result += chr(abs(((ord(c) + i - ord('a')) % 26)) + ord('a'))
        elif ord('A') <= ord(c) <= ord('Z'): #大文字の変換
            result = result + chr(abs(((ord(c) + i - ord('A')) % 26)) + ord('A'))
        else: #それ以外はそのまま出力
            result += c
    print (result)
    result = ""