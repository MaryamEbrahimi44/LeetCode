class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        k=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
                if nums1[i][0]==nums2[j][0]:
                    k.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                    i+=1
                    j+=1
                elif nums2[j][0]<nums1[i][0]:
                    k.append(nums2[j])
                    j+=1
                elif nums2[j][0]>nums1[i][0]:
                    k.append(nums1[i])
                    i+=1
        while i<len(nums1):
            k.append(nums1[i])
            i+=1
        while j<len(nums2):
                k.append(nums2[j])
                j+=1
        return k
            

        