class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        f, b = 0 , len(cleaned) - 1

        while f < b:
            if cleaned[b] != cleaned[f]:
                return False
            f+=1
            b-=1
        return True
