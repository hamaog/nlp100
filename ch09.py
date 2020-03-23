#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def typoglycemia(sentence9: str,sepValue=' '):
    words9 = sentence9.split(sepValue)
    words9_list = []
    for i in range(len(words9)):
        word9 = words9[i]
        if len(words9[i]) <= 4:
            words9_list.append(word9)
        else:
            word9_mod = word9[0] + ''.join(random.sample(word9[1:-1],len(word9[1:-1]))) + word9[-1]
            words9_list.append(word9_mod)
    return ' '.join(words9_list)

##文字列のシャッフルにはrandom.sampleが使える

sentence9_test1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typoglycemia(sentence9=sentence9_test1)
