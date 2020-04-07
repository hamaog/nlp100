#32. 動詞の原形
#動詞の原形をすべて抽出せよ．
#31. 動詞
#動詞の表層形をすべて抽出せよ．

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

##前問で一応いろんなパターンに耐えられる様にしておいたからあとは引数を変えるだけ
##だいぶ問題オリエンテッドだけどまぁ一旦よし

import collections

def mecab_parse_all_filter(parse_list,filter_key: str, append_word: str,wordclass: str):
    verbs = []
    for sentence in mecab_parse_all(filepath):
        for word in sentence:
            if word[f'{filter_key}'] == wordclass:
                verbs.append(word[f'{append_word}'])

    return sorted(collections.Counter(verbs).items(),key = lambda x:x[1],reverse=True)



filepath = '/Users/hamaokigaizaburo/Downloads/neko.txt.mecab'
mecab_parse_all_filter(mecab_parse_all(filepath),'pos','base','動詞')
