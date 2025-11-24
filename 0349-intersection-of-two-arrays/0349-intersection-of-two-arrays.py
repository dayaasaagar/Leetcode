class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin =[]
        i,j=0,0
        nums1.sort()
        nums2.sort()

        while i<len(nums1) and j <len(nums2):

            if nums1[i]==nums2[j]:
                if not fin or fin[-1]!=nums1[i]:
                    fin.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]<nums2[j]:
                i=i+1
            else:
                j=j+1
        return fin
            
            