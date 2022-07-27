"https://leetcode.com/problems/intersection-of-two-arrays-ii/"

# Fisrt Time 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        min_num = nums1 if len(nums1)<len(nums2) else nums2
        max_num = nums1 if len(nums1)>=len(nums2) else nums2
        res = {}
        ans = []
        
        for i in min_num:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        
        for j in max_num:
            if j in res and res[j] > 0:
                ans.append(j)
                res[j] -= 1 # key point!!!
        return ans
      
 # Second Time
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        long = []
        short = []
        if len(nums1)>len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        ref = {}
        for i in short:
            ref[i] = 1 + ref.get(i, 0)
        
        for j in long:
            if j in ref and ref[j]>0:
                ans.append(j)
                ref[j] -= 1
        return ans
        
