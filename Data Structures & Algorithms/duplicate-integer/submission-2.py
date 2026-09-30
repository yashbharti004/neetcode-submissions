class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = dic.get(num, 0) + 1
        for i in dic.values():
            if i > 1:
                return True
        return False