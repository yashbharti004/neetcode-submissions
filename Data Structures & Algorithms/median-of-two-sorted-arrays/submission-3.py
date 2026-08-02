class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            left = mid-1
            res = (nums[left]+nums[mid])/2
        else:
            res = nums[mid]
        return res