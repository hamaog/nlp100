#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

def file_GroupCount(fileName: str,columnNum: int):
    with open(fileName) as f:
        fileData = f.readlines()

    dataGroup = {}

    for data in fileData:
        key = data.split('\t')[columnNum-1]
        dataGroup[key] = dataGroup.get(key, 0) + 1

    return sorted(dataGroup.items(), key= lambda dataGroup: dataGroup[1],reverse=True)

directoryName = '/Users/***/hightemp.txt'
file_GroupCount(directoryName,1)

##本来ならpandasやcountを使うのかも、でもこっちのが軽そう
##lambdaはもうちょっと使いこなせると便利そう
##dictについても要復習

##UNIXコマンド
##sort < col1.txt | uniq -c | sort -k 1 -r
##UNIXにおいてもパイプはコマンドの受け渡しに使える
