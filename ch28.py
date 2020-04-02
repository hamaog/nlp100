#28. MediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

result28 = {}
for template_content in template_contents:
    ##強調除き
    value_str = re.sub(r"'{2,3}|'{5}", '',template_content[1])
    ##ファイル/カテゴリ含めた内部リンクの除去
    value_str = re.sub(r"\[\[(?:[^|].*?\|).*?([^|]*?)\]\]",r'\1',value_str)
    ##langの除去
    value_str = re.sub(r"\{\{(?:[^|]*?\|).*?([^|]*?)\}\}",r'\1',value_str)
    ##ref/brの除去
    value_str = re.sub(r"<\/?(ref|br)[^>]*?>",'',value_str)
    ##外部リンクの除去
    value_str = re.sub(r"\[(?:http)(?:[^\s].*?\s)?([^\]]*?)\]",r'\1',value_str)
    ##[]の除去
    value_str = re.sub(r"\[*?([^\[\]]*?)\]*?",r'\1',value_str)
    result28[template_content[0]] = value_str
    
##ちょっと所々漏れている気がする。。。ちゃんと関数組んで検討するべき
