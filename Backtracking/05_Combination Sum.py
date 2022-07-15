class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        self.__developingTree(0,candidates,[],target,answer)
        return answer
        
    def __developingTree(self, ci, candidates, temp, target,answer):
        if target == 0:
            answer.append( temp.copy() )
            return
        if target < 0:
            return
        if ci >= len(candidates):
            return
        
        
        temp.append( candidates[ci] )
        target -= candidates[ci]
        self.__developingTree(ci, candidates, temp, target,answer)
        
        temp.pop()
        target += candidates[ci]
        self.__developingTree(ci+1, candidates, temp, target,answer)
        