class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic1 = {}
        if len(s) == len(t):
            for a,b  in zip(s,t):
                if a not in dic:
                    dic[a] = dic.get(a, 0) + 1
                else:
                    dic[a] += 1
                if b not in dic1:
                    dic1[b] = dic1.get(b,0) + 1
                else:
                    dic1[b] += 1
        else:
            return False
        print(dic, dic1)
        if dic == dic1:
            return True
        return False