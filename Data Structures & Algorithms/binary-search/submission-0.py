class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        split = len(nums)//2

        if nums[split] > target:
            return self.search(nums[:split], target)
        
        if nums[split] < target: 
            result = self.search(nums[split+1:], target)
            return result + split + 1 if result > -1 else -1

        if nums[split]==target:
            return split
        else:
            return -1
        