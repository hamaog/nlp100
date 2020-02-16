# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

##めんどくさいので正規表現で置換してから数える様にした
##公式パッケージだけであれば、word.count()を地道に繰り返すっぽい
##このfor文の使い方は頻出だよなぁ。。。

import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split(' ')
result = []

for word in words:
    result.append(len(re.sub('(,|\.)','',word)))

result

##内包表記を使い、題意に丁寧に答えると以下
##isalphaでアルファベットか判定し、forに対して文字列をかけることで１文字ずつの判定リストを作って足し上げる
##こっちの方が全然いい

for word in words:
    count = sum([char.isalpha() for char in word])
    result.append(count)

result
