class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = []

        for i in s:
            if (i.isalnum()):
                stri.append(i.lower())
        j = len(stri) - 1
        k= 0
        if len(stri)<=1:
            return True
        while k < j:
            if stri[k] != stri[j]:
                return False
            k = k+1
            j = j-1
        return True