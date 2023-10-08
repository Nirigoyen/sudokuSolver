def findSpace(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


def checkValidNumber(number, board, col,
                     row):  # Un numero sera valido si ese numero no se encuentra ya en esa misma fila, columna o subcelda
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False

    initialRow, initialCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(initialRow, initialRow + 3):
        for j in range(initialCol, initialCol + 3):
            if board[i][j] == number:
                return False
    return True


def checkValidBoard(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:

                if board[row].count(board[row][col]) > 1:
                    return False

                if [board[x][col] for x in range(9)].count(board[row][col]) > 1:
                    return False

                initialRow, initialCol = 3 * (row // 3), 3 * (col // 3)
                subCell = [board[initialRow:initialRow + 3][initialCol:initialCol + 3]]
                if subCell.count(board[row][col]) > 1:
                    return False

    return True


def autosolve(board, show = 0):

    # Buscamos algun espacio vacio en el tablero
    row, col = findSpace(board)

    # Caso base: no quedan mas espacios libres en el tablero
    if row == None:
        return True

    # Probamos todos los numeros desde el 1 hasta el 9
    for num in range(1, 10):
        if checkValidNumber(num, board, col, row):
            # Si el numero es valido, asignamos a ese espacio libre el numero
            board[row][col] = num
            if show == 1:
                printBoard(board)

            # Llamado recursivo para poder avanzar en la resolucion
            if autosolve(board, show):
                return True

            # Si llegara hasta aca quiere decir que ese numero no sirvio, ponemos en 0 y procedemos con el backtracking
            board[row][col] = 0

    return False


def printBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


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

    print()
    print("Tablero ingresado: ")
    print()
    printBoard(board)

    if checkValidBoard(board):
        print()
        show = int(input("Quiere que se muestren los pasos intermedios? (1 para si, 0 para no): "))
        if autosolve(board, show):
            print()
            print("----------------------------------------------------")
            print("Resultado final: ")
            print()
            printBoard(board)
    else:
        print()
        print("----------------------------------------------------")
        print("El tablero ingresado no es valido para un sudoku.")
