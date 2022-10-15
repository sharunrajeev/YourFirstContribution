class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    li.append(i)
                    li.append(j)
        return li
