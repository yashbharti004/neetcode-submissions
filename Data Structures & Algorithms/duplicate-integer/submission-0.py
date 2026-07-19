class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        max = 0
        for i in nums:
            if i not in dic:
                dic[i] = dic.get(i, 0) + 1
            else:
                dic[i] += 1
        for i in dic.values():
            if i > max :
                max = i
        if max > 1:
            return True
        else:
            return False
            