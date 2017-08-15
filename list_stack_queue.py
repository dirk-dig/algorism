# coding: UTF-8
# list
list=["Eric", "John", "Michael", 66.25, 333, 333, 1, 1234.5]

#末尾追加
#listをスタックの用に扱える
list.append(20)
print list

#リスト拡張
#list.extend()

#指定位置要素挿入
list.insert(1,2.5)
print list

#最初の指定要素を削除
list.remove(1)
print list

#指定位置の要素を削除(初期:末尾)
#listをスタックの用に扱える
list.pop()
print list

#指定要素の位置を探索
list.index(333)
print list

#指定要素の回数
list.count(333)
print list

#リストの整列(初期値降順)
list.sort()
print list

#リストを逆順
list.reverse()
print list

# stack
stack=["Eric", "John", "Michael", 3, 4, 5]

#末尾追加
#listをスタックの用に扱える
stack.append(20)
print stack

#指定位置の要素を削除(初期:末尾)
#listをスタックの用に扱える
stack.pop()
print stack

# queue
# リストでは効率が悪い
from collections import deque
queue = deque(["Naoki", "James", "Ishibashi"])

#末尾追加
queue.append("Tanaka")
#先頭削除
queue.popleft()
