# -*- coding: utf-8 -*-
a = [1, 2, 3, 4]
b = []
c = []

def hanoi(n, frm, work, dest):
    global cnt
    if n < 1:
        return
    hanoi(n-1, frm, dest, work)
    print('{0:2}: {1}を{2}から{3}に移動したよ。'.format(cnt, n, frm, dest))
    cnt += 1
    hanoi(n-1, work, frm, dest)

hanoi(4, 'A', 'B', 'C')