#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

##コマンドラインの引数で受け取るっていうことは、ターミナルで.pyを実行する時に追加で指定するためのもの？
##実際の場面では大いにありそう、、、
##が、実感わかないので一旦スルー

import math

def file_ContSplit(fileName: str,sepNum: int):
##readlinesを使うと全部読み込むのでメモリを食うっぽい、、、

    with open(fileName) as f:
        fileData = f.readlines()

    merge_list_Num = math.ceil(len(fileData) / sepNum)

    for i in range(merge_list_Num):
        filename = '/Users/***/hightemp_split{0:02d}.txt'.format(i+1)
        with open(filename,'w') as f:
            f.write(''.join(fileData[i * merge_list_Num : (i+1) * merge_list_Num]))

directoryName = '/Users/***/hightemp.txt'

file_ContSplit(directoryName,5)

##UNIXコマンド
##split -l 5 hightemp.txt col1_split.
##UNIXコマンドで動的に扱う方法みたけどちょっと今はおいておく、いつかやれたら
##split -l $(expr $(wc -l col1.txt | awk '{print $1}') / 5) col1.txt col1_split.

##等分割にするっていうタスクがあったら、多分だけどスライサーのところまで小数点を待ってそこで切り上げる感じかな、？
