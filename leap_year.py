# coding: utf-8
def ly(a):
    return (a%4==0 and a%100!=0) or a%4==0

'''
if a%400 == 0:
    print "うるう年"

elif a%100 == 0:
    print"平年"

elif a%4 == 0:
    print "うるう年"

else:
    print"平年"
'''


print "西暦を入力"
a = int(input())
ly(a)