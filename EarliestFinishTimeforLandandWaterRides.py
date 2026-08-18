class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        result=float("inf")
        for i in range(len(landStartTime)):
            landfinish=landStartTime[i]+landDuration[i]
            for j in range (len(waterStartTime)):
                start=max(waterStartTime[j],landfinish)
                finish=start+waterDuration[j]
                result=min(result,finish)
        for i in range(len(waterStartTime)):
            waterfinish=waterStartTime[i]+waterDuration[i]
            for j in range(len(landStartTime)):
                start=max(waterfinish,landStartTime[j])
                finish=start+landDuration[j]
                result=min(result,finish)
        return result


        