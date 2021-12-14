import libnum

N = 
E = 65537

f = open('e_text.txt', 'rb') #バイナリファイルから読み込む想定
C = f.read()
f.close
C = int.from_bytes(C, 'big')

#素因数分解できたら
p = 
q = 
phi = (p-1)*(q-1)
d = pow(e, -1, phi) #秘密鍵

print(libnum.n2s(pow(C, d, N)))