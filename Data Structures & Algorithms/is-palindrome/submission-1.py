class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        n = s.replace(" ","")
        n = n.lower()
        for i in n:
            if i.isnumeric():
                return False
            if i.isalpha():
                res += i
        if res == res[::-1]:
            return True
        return False
