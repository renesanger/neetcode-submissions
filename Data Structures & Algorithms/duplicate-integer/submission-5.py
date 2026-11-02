class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = []
        for a in nums:
            if(a in m):
                return True
            m.append(a)


        return False;