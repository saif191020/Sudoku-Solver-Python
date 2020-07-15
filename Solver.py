#easy -2 ms
board = [
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,5,0,0,4,0],
    [4,6,0,0,0,1,2,9,5],
    [3,8,7,1,2,0,6,0,0],
    [5,0,1,7,0,3,0,0,8],
    [0,4,6,0,9,5,7,1,0],
    [9,1,4,6,0,0,0,8,0],
    [0,2,0,0,4,0,0,3,7],
    [8,0,3,5,1,2,0,0,4]
] 

#hard -2 sec
# board = [
#     [0,0,0,0,0,0,2,0,0],
#     [0,8,0,0,0,7,0,9,0],
#     [6,0,2,0,0,0,5,0,0],
#     [0,7,0,0,6,0,0,0,0],
#     [0,0,0,9,0,1,0,0,0],
#     [0,0,0,0,2,0,0,4,0],
#     [0,0,5,0,0,0,6,0,3],
#     [0,9,0,4,0,0,0,7,0],
#     [0,0,6,0,0,0,0,0,0]
# ]


def printBoard(b):
    '''
    prints a sudoku Board
    '''
    m = n =0
    for i in b:
        for j in i:
            if j !=0:
                print(j,"",end="")
            else:
                print(". ",end="")
            m=m+1
            if m%3==0 and m!=9:
                print("|",end="")
            if m==9:
                print("")
                m=0
        n=n+1
        if(n%3==0 and n!=9):
            print("---------------------")

def validator(b,i,j,no):
    '''checks if a number is possibe in the given space verticle/Horizontal/Box and returns true/Fasle \n\n b-board i-first index j-second index no-Number to check'''
    #Horizontal 
    if no in b[i]:
        return False
    #Verticle
    for k in range(0,9):
        if no == b[k][j]:
            return False
    #Box Check
    m=(i//3)*3
    n=(j//3)*3
    for r in range(m,m+3):
        for s in range(n,n+3):
            if no == b[r][s]:
                return False
    return True

def findEmpty(b):
    '''returns the position of empty space in tuple'''
    for i in range(0,9):
        if 0 in b[i]:
            ind = b[i].index(0)
            return (i,ind)
    return (-1,-1)

def solver(board):
    '''main solving logic'''
    (i,j) =findEmpty(board)
    if(i==-1 or j==-1):
        return 1
    for k in range(1,10):
        if(validator(board,i,j,k)):
            board[i][j]=k
            done=solver(board)
            if done == 1 :
                return 1
    board[i][j]=0
    return 0

printBoard(board)
solver(board)
print("")
printBoard(board) 