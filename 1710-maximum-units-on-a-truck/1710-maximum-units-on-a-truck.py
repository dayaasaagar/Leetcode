class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1],reverse=True)
        total=0

        for numboxes,numunit in boxTypes:

            if truckSize==0:
                break
            
            numberofboxes = min(truckSize,numboxes)
            total +=numberofboxes*numunit
            truckSize-=numberofboxes
        return total

