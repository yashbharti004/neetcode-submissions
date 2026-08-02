class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        mini = nums[0]
        right = len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            if nums[left] < mini:
                mini = nums[left]
            if nums[right] < mini:
                mini = nums[right]
            left += 1
            right -= 1

        return mini




        