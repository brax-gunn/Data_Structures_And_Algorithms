class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = []
        
        chessBoard = []
        for i in range(0, n):
            temp = []
            for j in range(0 , n):
                temp.append('.')
            chessBoard.append(temp)
        
        self.__recursionOnBoard(0, n, chessBoard, answer)
        
        return len(answer)
        
    def __recursionOnBoard(self, currentRow, n, chessBoard, answer):
        if currentRow >= n:
            temp = []
            for row in range(0, n):
                tempStr = ''
                for col in range(0, n):
                    tempStr+=chessBoard[row][col]
                temp.append(tempStr)
                    
            answer.append(temp.copy())
            return
        
        
        for col in range(0, n):
            if self.__isPosValid(currentRow, col, n, chessBoard):
                chessBoard[currentRow][col] = 'Q'
                self.__recursionOnBoard(currentRow+1, n, chessBoard, answer)
                chessBoard[currentRow][col] = '.'
                
        return

    def __isPosValid(self, currentRow, currentCol, n, chessBoard):
        # check in row
        for pos in range(0, n):
            if chessBoard[currentRow][pos] == 'Q':
                return False
        # check in column
        for pos in range(0, n):
            if chessBoard[pos][currentCol] == 'Q':
                return False
        # for diagonal top left
        currentX = currentRow
        currentY = currentCol
        while currentX >= 0 and currentY >= 0:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX -= 1
            currentY -= 1
        # for diagonal top right
        currentX = currentRow
        currentY = currentCol
        while currentX >= 0 and currentY < n:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX -= 1
            currentY += 1
        # for diagonal bottom left
        currentX = currentRow
        currentY = currentCol
        while currentX < n and currentY >= 0:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX += 1
            currentY -= 1
        # for diagonal bottom right
        currentX = currentRow
        currentY = currentCol
        while currentX < n and currentY < n:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX += 1
            currentY += 1
        
        return True