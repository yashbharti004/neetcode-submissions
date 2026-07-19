class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        cur = []
        seen = set()
        for i in range(len(strs)):
            dic = {}
            for k in strs[i]:
                if k not in dic:
                    dic[k] = dic.get(k , 0) + 1
                else:
                    dic[k] += 1
            res.append(dic)
        print(res)
        for i in range(len(res)):
            if i not in seen:
                n = [strs[i]]
            else:
                n = []
            seen.add(i)
            for j in range(i+1 ,len(res)):
                if res[j] == res[i] and j not in seen:
                    n.append(strs[j])
                    seen.add(j)
            if 0 != len(n):
                cur.append(n)
        return cur
                
         
            