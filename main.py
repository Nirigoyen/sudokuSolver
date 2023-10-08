
def getCell(row, col, board): #Averiguo en que subcelda se encuentra nuestra posicion a probar usando los limites de cada una de las subceldas
    colNum, rowNum = 0, 0
    limits = [0, 2, 5, 8]
    cells = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    for i in range(3):
        if not (limits[i] <= row <= limits[i + 1]):
            rowNum += 1

    for i in range(3):
        if not (limits[i] <= col <= limits[i + 1]):
            colNum += 1

    return cells[rowNum][colNum]

def checkInCell(number, cell, board):
    cases = { #Este diccionario contiene el desplazamiento que necesita cada subcelda para poder checkear cada posicion iterando 3 veces por fila
        1: (0, 0),
        2: (0, 3),
        3: (0, 6),
        4: (3, 0),
        5: (3, 3),
        6: (3, 6),
        7: (6, 0),
        8: (6, 3),
        9: (6, 6)
    }
    case = cases.get(cell)
    cellCounter = 0
    for i in range(3): #Iteramos 3 veces por fila comparando el numero que haya en esa posicion con el numero que estamos probando. Si llegamos a encontrar nuestro numero, retornamos true
        for j in range(3):
            if number == board[case[0] + i][case[1] + j]:
                cellCounter += 1
                
    if cellCounter <= 2:
        return False
    else:
        return True


def checkValidNumber(number, board, col, row): #Un numero sera valido si ese numero no se encuentra ya en esa misma fila, columna o subcelda
    # Checkeo que el numero no este en la fila en la que estamos tratando de colocar el numero
    if board[row].count(number) >= 2:
        inRow = True
    else:
        inRow = False

    # Checkeo que el numero no este en la columna en la que estamos tratando de colocar el numero
    inCol = False
    colCounter = 0
    for i in range(9):
        if number == board[i][col]:
            colCounter += 1
    if colCounter >= 2:
        inCol = True

    # Checkeo que el numero no este en la sub-celda en la que estamos tratando de colocar el numero
    inCell = checkInCell(number, getCell(row, col, board), board)

    return not inCol and not inCell and not inRow

def checkValidBoard(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                if not checkValidNumber(board[row][col], board, col, row):
                    return False
    return True
def autosolve(board):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in numbers:
                    if checkValidNumber(num, board, col, row):
                        board[row][col] = num
                        result = autosolve(board)
                        if result is not None:
                            return result
                    board[row][col] = 0
                return None
    return board

def printBoard(board):
    for row in board:
        print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    board = [[2, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 6, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(board)

    if checkValidBoard(board):
        print("El tablero ingresado no es valido para un sudoku.")
    else:
        result = autosolve(board)
        printBoard(result)
