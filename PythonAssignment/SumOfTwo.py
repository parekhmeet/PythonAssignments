"""  Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Input: nums = [1,3,7,21], target = 4
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 4, we return [0, 1]. """

class Solution(object):
    def SumOfTwo(self, nums, target):\

        """
        Write your logic here.
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