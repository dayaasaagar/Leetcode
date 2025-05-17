class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final=[]
        dict={}

        for i,num in enumerate(nums):
            if (target-num) in dict:
                #final.append(i)
                final.append(dict[target-num])
                final.append(i)

                return final

            else:
                dict[nums[i]]=i

            
        return []
            

        