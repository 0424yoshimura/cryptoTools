# RSA暗号
```
m : 平文 , c : 暗号文
公開鍵(e, n)
秘密鍵(d, n)
```
c = m^e mod n

m = c^d mod n
これが成り立つようなe, d, nを見つけたい！
```
e,d,nを見つける手順：
1. 2つの素数p.qを作る
2. n = p * qとする
3. φ(n) = (p - 1)*(q - 1) となる
4. eをφ(n)と素な適当な値に設定する，65537がよく使われる．
5. d = e^-1 mod φ(n) 分数ではなくmodの世界の逆数．
```
1.　素数p,qの作り方
p, qは 2^1024 とかのサイズを求められてる
⇨適当に乱数作って素数判定しよう！(エラトステネスの篩とかでは厳しい)
判定にはミラーラビンの素数判定法を使う，ちなみに計算量はO((log n)^3) 
素数の時は100%素数と判定する．合成数の時，3/4ほどの確率で合成数であると判定できる．1/4の確率で素数と判定してしまうのだが......（内部で乱数を使用しており，これによって結果が変わる）
じゃあたくさん回せば良くね？ということでめっちゃ回して全部素数だよ！ってなった時素数とする．間違える可能性は0に収束できる．(それでも既存のプログラムより早い)

3. φ(n)ってなに？
⇨オイラーのφ関数 : 1 ~ nまでの整数の中で，nと互いに素になるものの個数．
例 : φ(15) = (3 - 1)(5 -1) = 8
1,2,4,7,8,11,13,14が素だから合ってるね
ここですごいことに　a, nが互いに素な場合， a^φ(n) = 1 mod n ということが決まっている．

4. eについて
小さすぎたらだめ．e = 3とか　mod n取る前の値と一致しちゃってわかることある．mod回さないと全然難しい問題じゃない．（Low Public Exponent Attack）
大きすぎてもだめ．eに比べてdが相対的に小さい場合　Winer’s　Attackという攻撃が可能となる．
e = 65537 = 0b10000000000000001　であり，素数かつ計算がとっても楽
固定でもこれ公開鍵の情報だし安全だよね．
e,d入れ替えても成り立つよね？⇨成り立ちます．が，Winer’s　Attackができてしまいます．公開鍵と秘密鍵逆にしちゃダメ．
秘密鍵から公開鍵求めることは可能，逆は不可能．

http://www.factordb.com/
とりあえずNが素因数分解出来ないかここで試しておこう
