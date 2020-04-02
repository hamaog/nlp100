#27. 内部リンクの除去
#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
result27 = {}
for template_content in template_contents:
    result27[template_content[0]] = re.sub(r"'{2,3}|'{5}", '',template_content[1])
    result27[template_content[0]] = re.sub(r"\[\[(?:[^|]*?\|).*?([^|]*?)\]\]",r'\1',result27[template_content[0]])

##パイプの一番後ろをとってくる必要がある(内部リンクは複数のパイプで繋がれることがある)
