#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import urllib.request
import json

filename = result28["国旗画像"]
r_url = 'https://www.mediawiki.org/w/api.php?{}'
params = {
    'action': 'query',
    'format': 'json',
    'prop': 'imageinfo',
    'titles': 'File:{}'.format(filename),
    'iiprop': 'url'
}

req = urllib.request.Request(r_url.format(urllib.parse.urlencode(params)))
with urllib.request.urlopen(req) as res:
    response_j = json.loads(res.read())

img_url = response_j['query']['pages']['-1']['imageinfo'][0]['url']
