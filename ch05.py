#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

##ngramの単位は複数あるっぽい(文字,形態素,品詞)
##http://www.ic.daito.ac.jp/~mizutani/mining/n_gram.html
##問題文の単語と文字、というのがおそらく、品詞と文字のことだと思う
##とすると、与えられた文章に対して何で分かつのか、と分けたあとのngramを作る関数で分けた方がいいはず


##任意で分かつための関数
##引数をオプション化する方向はあまりなく、基本はデフォルト値を入れて中で無視するのが良いらしい
def wakati(sentence,sepType,sepValue=''):
    ##学習の分かりやすさのために引数を置き換えずchar/wordと直接書く、本番は絶対にしない
    if(sepType == 'char'):
        return list(sentence5)
    elif(sepType == 'word'):
        return sentence.split(sepValue)
    ##if文の中でtryみたいなエラーの吐き出させ方を知りたい
    else:
        return 'Error'

##任意で切った後にngramの処理
##リストに対して、任意数の単位で分割を行う
def ngram(word_list,byN):
    return [word_list[idx:idx+byN] for idx in range(len(word_list) - byN + 1)]

sentence5 = "I am an NLPer"

ngram(wakati(sentence5,'char'),2)
ngram(wakati(sentence5,'word',' '),2)

ngram(wakati(sentence5,'char'),3)
ngram(wakati(sentence5,'word',' '),3)
