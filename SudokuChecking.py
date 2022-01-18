def isSafe(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def findUnassignedPosition():
    for i in range(0,9):
        for j in range(0,9):
            if(sudokuTable[i][j] == 0):
                return (i,j)
    return None
def solveSudoku():
    find = findUnassignedPosition()
    if(find == None):
        return True
    row,col = find[0],find[1]
    print(row,col)
    for num in range(1,10):
        if(isSafe(sudokuTable,row,col,num)):
            sudokuTable[row][col] = num
            if(solveSudoku()):
                return True
            sudokuTable[row][col] = 0
    return False
