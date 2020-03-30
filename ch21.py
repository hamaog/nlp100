#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．

UK = articles['イギリス']
category_list = [text for text in UK.split('\n') if '[[Category:' in text]
##カテゴリというのはその記事がどのカテゴリに属する記事かというのを表すメタ的な情報
##末尾の方にある
