#04. 元素記号
#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

##他の人の回答も見たものの、自分的にしっくりこないのが主に２点

##1.マスタを自分で作りたくない(今回の場合1,5,6などと決まっているものに対して、2,3,4などと新たに補完するマスタを作りたくない、元素周期表などはより一層)
###単純にミスった時に検算しなきゃいけない項目が多いのが実用的ではないと思った

##2.思惑としては元素周期表を作りたいとのことだったので、順番にもこだわるべきだと思った(この場合は元の文の順番を崩してはいけない)ので、ハッシュ関数を用いるものはやめたい
###まぁ出来上がったものをソートすればいいのかもだけど、、、
###https://qiita.com/segavvy/items/4e592dea2f828e5385ff
###上記のコメント欄にあるordereddictは使えそう

sentence4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words4 = sentence4.split(' ')

cond4_temp = [1, 5, 6, 7, 8, 9, 15, 16, 19]
cond4 = list(map(lambda x:x-1,cond4_temp))

##if使う方
result4 = {}
for i,word4 in enumerate(words4,1):
    if(words4.index(word4) in cond4):
        result4[word4[0]] = i
    else:
        result4[word4[:2]] = i
print(result4)


##できるだけ記述量を減らしたいというか、1文字か2文字かを判定するなら1行ですむかなと書いてみる、自己満
##2値だからいいけど3値以上になった時にどうするかだよなー、

result4 = {}
for i,word4 in enumerate(words4,1):
    endChar = 2 - int(words4.index(word4) in cond4)
    result4[word4[0:endChar]] = i

print(result4)

##はじめindexの取得を.indexでやってたけど、要素の被りは全然ありえると思ったのと記述を楽にするためにenumarateを使用した、すっきり
testSentence4 = "Hi He Lied Hi"
testWords4 = testSentence4.split(' ')

for testWord4 in testWords4:
    print(testWords4.index(testWord4))

for i,testWord4 in enumerate(testWords4):
    print(i)

##ちなみに速度を計測すると
##ifで分ける方      158 µs ± 5.53 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
##ifで分けない方    157 µs ± 8.07 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
##大して変わらないし、場合によっては分ける方が安定したパフォーマンスになりそう、実用に載せるならif使う一択ぽい
