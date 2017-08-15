#coding: UTF-8

f = open('practice.txt')
data = f.read()
f.close()
lines = data.split()
# 引数に何も指定しない場合、スペースやタブ等で自動的に区切る
print lines

