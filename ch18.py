#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

def file_ColumnSortDesc(fileName: str,columnNum: int):
    with open(fileName) as f:
        fileData = f.readlines()
    return sorted(fileData, key=lambda fileData: fileData.split('\t')[columnNum-1],reverse=True)

directoryName = '/Users/***/hightemp.txt'
file_ColumnSortDesc(directoryName,3)

##lambdaは無名関数として、使い回しをしない様なタイミングで使う
##sortedのkeyはリストでも文字でもいける

##UNIXコマンド
##sort -k 3 -r hightemp.txt
##キーkを指定しつつ降順rで並び替えする
