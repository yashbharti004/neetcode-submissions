class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = []

        cur = [] 
        left = 0
        right = 0
        for i in s1:
            seen.append(i)
        while left < len(s2) - len(s1) + 1:
            while right < (left + len(s1)):
                cur.append(s2[right])
                right += 1
            
            if sorted(seen) == sorted(cur):
                return True
            cur.remove(s2[left])
            left += 1
        return False