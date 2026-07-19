class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = [] 
        for i in nums:
            if i not in dic:
                dic[i] = dic.get(i , 0) + 1
            else:
                dic[i] += 1
        for i in range(k):
            max = 0
            cur = 0
            for j in dic:
                if dic[j] > max:
                    max = dic[j]
                    cur = j
            res.append(cur)
            dic[cur] = 0
        return res
