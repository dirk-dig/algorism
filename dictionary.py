# coding: UTF-8
dic = {"Naoki":170, "Kiichi":180, "Takeshi":170, "Naomi":160}
print dic

# keyの一覧取得
print dic.keys()

# valueの一覧取得
print dic.values()

# keyとvalueの一覧取得
print dic.items()

#要素削除
del dic["Naoki"]
print dic
#要素追加
dic["James"]=200
print dic
#連結
dic2 = {'grape': 300, 'melon': 500, 'peach': 200}
dic.update(dic2)
print dic
