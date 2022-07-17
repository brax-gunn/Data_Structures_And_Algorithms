def displayBoard(chess):
    for i in range(len(chess)) :
        for j in range(len(chess)) :
            print(chess[i][j], "", end = '');
        print()
    print()


def knightTour(chess, currentRow, currentCol, upComingMove, n):
    if(upComingMove == n*n+1):
        displayBoard(chess)
        return

    if currentRow < 0 or currentRow >= n or currentCol < 0 or currentCol >= n or chess[currentRow][currentCol] != 0:
        return

    chess[currentRow][currentCol] = upComingMove

    knightTour(chess, currentRow-2, currentCol+1, upComingMove+1, n)
    knightTour(chess, currentRow-1, currentCol+2, upComingMove+1, n)
    knightTour(chess, currentRow+1, currentCol+2, upComingMove+1, n)
    knightTour(chess, currentRow+2, currentCol+1, upComingMove+1, n)
    knightTour(chess, currentRow+2, currentCol-1, upComingMove+1, n)
    knightTour(chess, currentRow+1, currentCol-2, upComingMove+1, n)
    knightTour(chess, currentRow-1, currentCol-2, upComingMove+1, n)
    knightTour(chess, currentRow-2, currentCol-1, upComingMove+1, n)
   
    chess[currentRow][currentCol] = 0
    



def main():
    n = int(input());
    chess = [];
    for i in range(n) :
        a = [];
        for j in range(n) :
            a.append(0);
        chess.append(a);
    row = int(input());
    col = int(input());
    knightTour(chess, row, col, 1, n);
    
main()