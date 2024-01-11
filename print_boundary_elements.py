def boundary_elements(a):
    row = len(a)
    col = len(a[0])

    if row == 1:
        for i in range(row):
            print(a[0][i] ,end=" ")

    if  col == 1:
        for i in range(col):
            print(a[i][0] ,end=" ")

    else:
        for i in range(row):
            print(a[0][i] ,end=" ")

        for i in range(1,col):
            print(a[i][row-1],end=" ")

        for i in range(row-2,-1,-1):
            print(a[row-1][i],end=" ")

        for i in range(row-2,0,-1):
            print(a[i][0],end=" ")


a =[[1,2,3,4],[5,6,7,8] ,[9,10,11,12],[13,14,15,16]]
boundary_elements(a)


    