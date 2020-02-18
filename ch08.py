#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence8: str):
##strとして処理を前提とする、アノテーション関数といい3.5以降の実装
##これも実際の効力はないっぽい、ただの注釈
    sentence8_cipher = ''

    for i in sentence8:
        if i.islower():
            sentence8_cipchr = chr(219 - ord(i))
        else:
            sentence8_cipchr = i
        sentence8_cipher += sentence8_cipchr

    return sentence8_cipher

sentence8_test1 = 'a1a2a345'
cipher(sentence8_test1)
