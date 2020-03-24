#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ

def countLine(directoryName: str):
    count = 0
    with open(directoryName) as f:
        for line in f:
            count += 1
    return count

fileName = '/Users/hamaokigaizaburo/Downloads/hightemp.txt'
countLine(fileName)

#UNIXコマンドでの確認
#ターミナルで実行、-lを付けなければ単語数やバイト数も表示される
#wc -l /Users/hamaokigaizaburo/Downloads/hightemp.txt
