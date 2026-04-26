class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window = {}
        for c in s2[:len(s1)]:
            window[c] = window.get(c, 0) + 1

        if window == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            window[new_char] = window.get(new_char, 0) + 1
            old_char = s2[i - len(s1)]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]
            if window == s1_count:
                return True 
        return False
        