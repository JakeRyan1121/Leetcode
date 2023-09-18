from typing import List

class Solution:

    def containsDuplicatej(self, nums: List[int]) -> bool:
        newset = {}
        for i in nums:
            newset.add(i)
        if len(nums) == len(newset):
            return False
        return True


    def containsDuplicater(self, nums: List[int]) -> bool:
        newset = set()

        for i in nums:
            if i in newset:
                return True
            else:
                newset.add(i)

        return False

sol = Solution()
print(sol.containsDuplicater([1, 3, 3, 4]))
#print(sol.containsDuplicatej([1, 2, 4, 4, 5]))