def spiral(a):
    row = len(a)
    col = len(a[0])
    for i in range(row):
        print(a[0][i], end=" ")

    for i in range(1,row):
        print(a[i][row-1],end=" ")

    for i in range(row-2,-1,-1):
        print(a[row-1][i],end=" ")

    for i in range(row-2,0,-1):
        print(a[i][0],end=" ")
    for i in range(1,row-1):
        print(a[1][i] ,end=" ")
    for i in range(row-2,0,-1):
        print(a[row-2][i],end=" ")

a = [[1,2,3,4],[5,6,7,8] ,[9,10,11,12],[13,14,15,16]]
spiral(a)
