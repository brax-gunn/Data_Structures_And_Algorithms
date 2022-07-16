class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.__sudokuSolver(0, 0, board)
        return
    
    def __sudokuSolver(self, currentRow, currentCol, board):
        
        if currentRow == 9:
            return True
        
        if currentCol == 8:
            nextRow = currentRow + 1
            nextCol = 0
        else:
            nextRow = currentRow
            nextCol = currentCol + 1
            
        if board[currentRow][currentCol] != ".":
            return self.__sudokuSolver(nextRow, nextCol, board)
        
        for num in range(1,10):
            if self.__isValidCell(currentRow, currentCol, str(num), board):
                board[currentRow][currentCol] = str(num)

                if self.__sudokuSolver(nextRow, nextCol, board) is True:
                    return True

                board[currentRow][currentCol] = "."
        
        return False
    
    def __isValidCell(self, currentRow, currentCol, value, board):
        
        # check in row
        for col in range(9):
            if board[currentRow][col] == value:
                return False
            
        # check in col
        for row in range(9):
            if board[row][currentCol] == value:
                return False
        
        # check in box
        startRow = 3 * (currentRow // 3)
        startCol = 3 * (currentCol // 3)
        
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == value:
                    return False
        return True