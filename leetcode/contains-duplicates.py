# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

'''
Time complexity: O(n)
where n = size of nums

Space Complexity: O(n)
where n = size of nums
'''
