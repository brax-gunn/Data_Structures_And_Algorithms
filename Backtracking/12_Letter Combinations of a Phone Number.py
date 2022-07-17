class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        ans = []
        if len(digits) <= 0:
            return ans
        self.__generateCombination(digits, 0, memo, '', ans)
        return ans
    
    def __generateCombination(self, digits, currentIndex, memo, myStr, ans):
        if currentIndex >= len(digits):
            ans.append(myStr)
            return
        
        
        for elem in memo[digits[currentIndex]]:
            self.__generateCombination(digits, currentIndex+1, memo, myStr+elem, ans)
            
        return