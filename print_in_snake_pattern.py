def snake_pattern(matrix):
    for i in range(len(matrix)):
        if i%2==0:
            for j in range(len(matrix)):
                print(matrix[i][j] , end=" ")

        else:
            for j in range(len(matrix)-1,-1,-1):
                print(matrix[i][j] , end=" ")


a = [[1,2,3,4],[5,6,7,8] ,[9,10,11,12],[13,14,15,16]]
snake_pattern(a)
