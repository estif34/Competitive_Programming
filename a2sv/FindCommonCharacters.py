class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res = []
        word1 = set(words[0])
        for char in word1:
            freq = min(word.count(char) for word in words)
            res += [char] * freq
        return res
