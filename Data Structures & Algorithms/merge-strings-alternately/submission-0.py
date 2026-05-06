class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        l = 0
        r = 0
        

        while l < len(word1)  and r < len(word2):
            merged.append(word1[l])
            l += 1
            merged.append(word2[r])
            r += 1
        merged.append(word1[l:])
        merged.append(word2[r:])
        return "".join(merged)
        
        