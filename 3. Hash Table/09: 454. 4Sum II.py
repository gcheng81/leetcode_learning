"https://leetcode.com/problems/4sum-ii/"

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = {}
        count = 0
        for i in nums1:
            for j in nums2:
                total = i+j
                if total not in record:
                    record[total] = 1
                else:
                    record[total] += 1
        
        for i in nums3:
            for j in nums4:
                target = 0-(i+j)
                if target in record:
                    count += record[target]
        
        return count
        
