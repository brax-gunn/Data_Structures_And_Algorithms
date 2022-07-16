class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value != ".":
                    board[row][col] = "."
                    if self.__isValidCell(row, col, value, board) == False:
                        return False
                    board[row][col] = value
        return True
    
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