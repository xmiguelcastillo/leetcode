class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        i = 0
        min_size = min(len(word1), len(word2))
        while i < min_size:
            output += word1[i]
            output += word2[i]
            i += 1
        output += word1[i:]
        output += word2[i:]

        return output
