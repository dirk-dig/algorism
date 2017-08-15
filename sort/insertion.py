# code UTF-8
x= [5, 2, 4, 6, 1, 3]
A = map(int,raw_input("数列:").split(','))

for i in range(1,len(A)):
    if A[i-1]