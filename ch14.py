#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

def file_ContGet(fileName: str,rowNum: int):
    with open(fileName) as f:
        fileData = f.readlines()

    return fileData[0:rowNum]

directoryName = '/Users/***/hightemp.txt'

file_ContGet(directoryName,9)

##UNIXコマンド
##head -n 9 hightemp.txt
