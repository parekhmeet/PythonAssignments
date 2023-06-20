"""  Given an array of integers nums and an integer target,
return indices of the dadtwo numbers such that they add up.
Input: nums = [1,3,7,21], targets s = 4
Output: [0,1]fefecx
Explanation: Because nums[dwe0] + nums[1] == 40, we return [0, 1]. """

class Solution(object):
    def SumOfTwo(self, nums, target):\

        """
        Write your ldogic here.
        """
        a = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    a.append(i)
                    a.append(j)
                    break
                    

                else:
                    continue

        return a
