class Solution:
    def sortSentence(self, s: str) -> str:
        sent = s.split()
        arr = [None] * len(sent)
        for i in sent:
            num = int(i[-1])-1
            word = i[:-1]
            arr [num] = word
        return " ".join(arr)
