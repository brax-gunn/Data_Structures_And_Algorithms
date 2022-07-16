class Solution:
    def findPath(self, m, n):
        allPath = []
        self.__moveRat(0, 0, n-1, n-1, m, "", allPath)
        return allPath
    
    def __moveRat(self, currR, currC, endR, endC, arr, currPath, allPath):
            
        if currR < 0 or currR > endR or currC < 0 or currC > endC:
            return
        
        if arr[currR][currC] == 0:
            return
        
        if currR == endR and currC == endC:
            allPath.append(currPath)
            return

        arr[currR][currC] = 0
        
        # move down
        self.__moveRat(currR+1, currC, endR, endC, arr, currPath+"D", allPath)
        
        # move right
        self.__moveRat(currR, currC+1, endR, endC, arr, currPath+"R", allPath)
        
        # move up
        self.__moveRat(currR-1, currC, endR, endC, arr, currPath+"U", allPath)
        
        # move left
        self.__moveRat(currR, currC-1, endR, endC, arr, currPath+"L", allPath)
        
        arr[currR][currC] = 1
        
        return