#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．

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

def mecab_parse_all(filepath):
    parse_texts_list = list(mecab_read_file(filepath))
    return parse_texts_list


def mecab_AnoB_word(filepath):
    words = []
    for sentence in mecab_parse_all(filepath):
        if len(sentence)>2: #EOS除く
            for i in range(1,len(sentence)-1): #enumerateも検討したが、リスト最初と末尾を除く文字数を考えるとこっちのが良かった
                if (sentence[i]['surface'] == 'の'
                    and sentence[i-1]['pos'] == '名詞'
                    and sentence[i+1]['pos'] == '名詞'
                    ):
                    words.append(   sentence[i-1]['surface']
                                    +sentence[i]['surface']
                                    +sentence[i+1]['surface']
                                    )
    return words



filepath = '/Users/***/neko.txt.mecab'
mecab_AnoB_word(filepath)
