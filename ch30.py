#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．


def mecab_description(mecabline):
    (surface, attr) = mecabline.split('\t')
    arr = attr.split(',')
    return {
        'surface':surface,
        'base':arr[6],
        'pos':arr[0],
        'pos1':arr[1]
    }

def mecab_read_file(filepath):

    mecab_sentence = []
    with open(filepath,mode='rt',encoding='utf8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line == 'EOS':
                ##このyield⇨空にする処理によってEOSによって格納されるlistが変わって出力される
                yield mecab_sentence
                mecab_sentence = []
            else:
                ##ここではリストに対して各パース結果が辞書で格納される
                mecab_sentence.append(mecab_description(line))

def mecab_parse_line(filepath,lineNum):
    parse_texts = list(mecab_read_file(filepath))[lineNum]
    linetext = ''.join([i['surface'] for i in parse_texts])
    return {'lineNum':lineNum,
            'text':linetext,
            'parse_result':parse_texts}


filepath = '/Users/hamaokigaizaburo/Downloads/neko.txt.mecab'
mecab_parse_line(filepath,3)

##文末では EOS
##それ以外の行は表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

##sentenceと文を別のリストとして処理する例も結構ある
##ここでは、最終的に何文目かで抜き出したい場面が多いはず、そのためには結局EOSで区切られたあとの判定が必要
## (全形態素の解析が終わったあとじゃないと判断できない)⇨結局全部読みこむので、メモリを食わないyieldの方が良いのではと判断
