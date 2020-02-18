#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

word61 = "paraparaparadise"
word62 = "paragraph"

##まずは05の関数を流用

##任意で分かつための関数
##引数をオプション化する方向はあまりなく、基本はデフォルト値を入れて中で無視するのが良いらしい
def wakati(sentence,sepType,sepValue=''):
    ##学習の分かりやすさのために引数を置き換えずchar/wordと直接書く、本番は絶対にしない
    if(sepType == 'char'):
        return list(sentence)
    elif(sepType == 'word'):
        return sentence.split(sepValue)
    ##if文の中でtryみたいなエラーの吐き出させ方を知りたい
    else:
        return 'Error'

##任意で切った後にngramの処理
##リストに対して、任意数の単位で分割を行う
def ngram(word_list,byN):
    return [''.join(word_list[idx:idx+byN]) for idx in range(len(word_list) - byN + 1)]


##https://note.nkmk.me/python-set/
##listをユニークにまとめたsetを作成した後に、各種演算子を使う

set61 = set(ngram(wakati(word61,'char'),2))
set62 = set(ngram(wakati(word62,'char'),2))

##和集合
set61 | set62
##積集合
set61 & set62
##差集合
set61 - set62
set62 - set61
##一応排他的論理和、演算子の処理順も兼ねて2パターンで検証
(set61 - set62) | (set62 - set61)
set61 ^ set62

##要素が含まれるかはinで良い
'se' in set61
'se' in set62
