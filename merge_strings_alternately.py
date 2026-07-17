class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        minlen= min(len(word1),len(word2))
        maxlen= max(len(word1),len(word2))
        i=0
        while i <minlen:
            result.append(word1[i])
            result.append(word2[i])
            i+=1
        if len(word1)==maxlen:
            result.append(word1[i:])
        else:
            result.append(word2[i:])
        return "".join(result)
            

        