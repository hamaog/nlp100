#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

def file_ColumnUniq(fileName: str,columnNum: int):
    with open(fileName) as f:
        fileData = f.readlines()

    return list(set([rowCont.split('\t')[columnNum-1] for rowCont in fileData]))


directoryName = '/Users/***/hightemp.txt'

file_ColumnUniq(directoryName,1)

##UNIXコマンド
##macのターミナルだと--のoptionが使えないっぽい
##cut --fields=1 hightemp.txt | sort | uniq > result_test.txt
##そこで以下の回答があったものの、元ファイルにアクセスしたい。。。
##UNIXで他のコマンドの出力を引数にしたい時って関数組む感じなんですかね？
##cat col1.txt | sort | uniq
