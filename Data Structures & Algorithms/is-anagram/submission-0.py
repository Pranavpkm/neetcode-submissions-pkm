class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()

        for s in str:
            hashset.add(s)
        if s in hashset:
            return True
        return False
        