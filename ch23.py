#23. セクション構造
#記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
section_list = [section for section in re.findall(r'^(=+)(.+?)\1$',UK,flags=re.MULTILINE)]

for section in section_list:
    print('{}:{}'.format(section[1].strip(),len(section[0])-1))

##reライブラリで「改行ごとに行頭・行末として扱う」ためには、re.MULTILINEを指定
