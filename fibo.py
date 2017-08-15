def fibonach(x):
    if x <= 1:
        return 1
    else:
        return fibonach(x-1)+fibonach(x-2)

for i in range(0,10):
    print fibonach(i)

