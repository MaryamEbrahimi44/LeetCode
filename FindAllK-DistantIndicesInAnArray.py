class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> List[int]:
        last=-1
        ans=[]
        for i,x in enumerate(nums):
            if x==key:
                start=max(i-k,last+1)
                end=min(i+k,len(nums)-1)
                for j in range(start, end+1):
                    ans.append(j)
                last=end
        return ans

        