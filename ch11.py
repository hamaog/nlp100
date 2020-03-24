#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

def file_translate(bef_directoryName: str,aft_directoryName: str,bef,aft):
    with open(bef_directoryName) as f:
        data_lines = f.read()

    with open(aft_directoryName, mode="w") as f:
        f.write(data_lines.replace(bef,aft))

bef_fileName = '/Users/***/hightemp.txt'
aft_fileName = '/Users/***/hightemp_upd.txt'

file_translate(bef_fileName,aft_fileName,'\t',' ')

##タブは\tで入力する方が諸々の設定の影響を受けなくて良さそう

#UNIXコマンドでの確認
##sed -e 's/\t/ /g' /Users/***/hightemp.txt
##tr '\t' ' ' < /Users/***/hightemp.txt

##tr便利だったけど、汎用性はsedの方が高いっぽい？UNIXを使った方がファイルの容量や環境に依存しなさそうなのでタイミングで復習
