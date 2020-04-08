#33. サ変名詞
#サ変接続の名詞をすべて抽出せよ．

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

import collections

def mecab_parse_all_filter(parse_list):
    verbs = []
    for sentence in mecab_parse_all(filepath):
        for word in sentence:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                verbs.append(word['base'])

    return sorted(collections.Counter(verbs).items(),key = lambda x:x[1],reverse=True)

filepath = '/Users/hamaokigaizaburo/Downloads/neko.txt.mecab'
mecab_parse_all_filter(mecab_parse_all(filepath))

##ほんとは引数に辞書を持たせて自由にfilterをかける方法をやりたかった、、調ベ方が悪く出てこないので再検討
