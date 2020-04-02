#26. 強調マークアップの除去
#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

result26 = {}
for template_content in template_contents:
    result26[template_content[0]] = re.sub(r"'{2,3}|'{5}", '',template_content[1])
