class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=word.find(ch)
        res=word
        if i != -1:
            res=word[i::-1]+word[i+1:]
        return res

        