def tranpose_matrix(a):
    row = len(a)
    col = len(a[0])
    temp = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            temp[j][i] = a[i][j]

    print(temp)




a = [[1,2,3,4],[5,6,7,8] ,[9,10,11,12],[13,14,15,16]]
tranpose_matrix(a)
