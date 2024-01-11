def ninet_degree_rotation(matrix):
    row = len(matrix)
    col = len(matrix[0])
    temp = [[0]*col for i in range(row)]

    for i in range(row):
        for j in range(col):
            temp[row-j-1][i] = matrix[i][j]

    print(temp)


a = [[1,2,3,4],[5,6,7,8] ,[9,10,11,12],[13,14,15,16]] 
ninet_degree_rotation(a)