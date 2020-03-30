#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
import os
import gzip
import json

def load_gzip_json(fileName):
    with gzip.open(fileName, 'rt',encoding='utf8') as f:
        return {item['title']:item['text'] for item in [json.loads(content)for content in f]}

directoryName = '/Users/***/'
os.chdir(directoryName)
fileName = 'jawiki-country.json.gz'

articles = load_gzip_json(fileName)
articles['イギリス']
