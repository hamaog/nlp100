#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
##この上の方にある基礎情報を辞書として抜き出すことが目的
UK.split("\n")[:100]

template_contents_text = [media for media in re.findall(r'^\{\{基礎情報(.*?)^\}\}$',UK,re.MULTILINE + re.DOTALL)]
##.*?とすることで非貪欲マッチとなり、改行含め最初に対応する}}を呼び出すことができる
##multilineとdotallを使うことで改行を行頭と行末のみの{}を対象とすることができる
##この際、キャプチャ部分は改行等を超える様、？

template_contents = [content for content in re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))',template_contents_text[0],re.MULTILINE + re.DOTALL)]
##後半の非キャプチャ部分を持ってくることで２個目のキャプチャ対象に必要な情報を全て入れる
##後半の非キャプチャ部分は、次のコンテンツの始まりか、文末で終わりを明示している

result = {}
for template_content in template_contents:
    result[template_content[0]] = template_content[1]
