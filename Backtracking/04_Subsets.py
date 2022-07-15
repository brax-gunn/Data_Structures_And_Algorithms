class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        self.__generateSubset(nums,0,len(nums),[], allSubsets)
        return allSubsets
    
    def __generateSubset(self,nums,ci,n,temp, allSubsets):
        if ci >= n:
            allSubsets.append(temp.copy())
            return
        
        
        temp.append( nums[ci] )
        self.__generateSubset(nums,ci+1,n, temp, allSubsets)
        
        temp.pop()
        self.__generateSubset(nums,ci+1,n,temp, allSubsets)