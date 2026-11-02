class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        freq = {}

        for i in range(len(nums)):
            if(nums[i] in freq):
                result = True
                break
            else:
                freq[nums[i]] = 1


        return result


        ''' 
            Kenneth solution
            two pointers i,j
            two loops
            bubble search
        '''

        '''
            sliding window
        '''

        '''
            hashmap
        '''