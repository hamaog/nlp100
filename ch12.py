#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

def file_extract(directoryName: str,sepValue: str,num1,num2):
    with open(directoryName) as f:
        data_lines = f.readlines()

    col1 = '\n'.join([data_line.split(sepValue)[num1-1] for data_line in data_lines])
    col2 = '\n'.join([data_line.split(sepValue)[num2-1] for data_line in data_lines])

    with open(f'/Users/***/col{num1}.txt', mode='w') as f:
        f.write(col1)

    with open(f'/Users/***/col{num2}.txt', mode='w') as f:
        f.write(col2)

num1 = 1
num2 = 2
directoryName = '/Users/***/hightemp.txt'

file_extract(directoryName,'\t',1,2)

##UNIXコマンド
##cut -f 1 hightemp.txt
##cut -f 2 hightemp.txt
