#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

def file_merge(bef_file1: str,bef_file2: str,aft_file: str,sepValue: str):
    with open(bef_file1) as f:
        data1 = f.readlines()

    with open(bef_file2) as f:
        data2 = f.readlines()

    data_merge = ['{}\t{}\n'.format(data11.strip(),data21.strip()) for data11,data21 in zip(data1,data2)]

    with open(aft_file,'w') as f:
        f.write(data_merge)

bef_file1 = '/Users/***/col1.txt'
bef_file2 = '/Users/***/col2.txt'
aft_file =  '/Users/***/col_merge.txt'

file_merge(bef_file1,bef_file2,aft_file,'\t')

##UNIXコマンド
##paste col1.txt col2.txt
