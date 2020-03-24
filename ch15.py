#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

def file_ContGetFromTail(fileName: str,rowNum: int):
    with open(fileName) as f:
        fileData = f.readlines()

    return fileData[-rowNum:]

directoryName = '/Users/***/hightemp.txt'

file_ContGetFromTail(directoryName,9)

##実際にやることがあるなら開始行と終了行書かせて14とマージした関数を作る

##UNIXコマンド
##tail -n 9 hightemp.txt
