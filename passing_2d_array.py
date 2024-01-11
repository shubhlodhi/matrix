def matrix(mat):
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        for j in range(c):
            print(mat[i][j] ,end=" ")

if __name__=='__main__':
    mat = [[1,0] , [2,9,9] ,[3,0]]
    matrix(mat)

    


    