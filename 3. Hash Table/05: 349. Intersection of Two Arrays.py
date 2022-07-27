"https://leetcode.com/problems/intersection-of-two-arrays/"

# Solution 1: Dictionary
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        for i in range(len(short)):
            ref[short[i]] = 1 + ref.get(short[i], 0)
        
        for j in range(len(long)):
            if long[j] in ref.keys():
                ans.append(long[j])
        return set(ans)
 
# Solution 2: Set
# (1) Two Sets
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        min_num = nums1 if len(nums1)<len(nums2) else nums2
        max_num = nums1 if len(nums1)>=len(nums2) else nums2
        
        min_num = set(min_num)
        max_num = set(max_num)
        res = []
        
        for i in min_num:
            if i in max_num:
                res.append(i)
        return res
 
# (2) Built-in Set Intersection
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
