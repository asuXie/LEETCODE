class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(0, len(nums)):
            
            for j in range(0, len(nums)):
               
                if nums[i] + nums[j] == target and j != i:
                    result.append(i)
                    result.append(j)
                    break
            if len(result) != 0:
                break
        print(result)
        return result


