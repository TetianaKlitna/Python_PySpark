# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Brute Force
    # max_sum = float('-inf')
    # for start in range(len(nums)):
    #     for end in range(start,len(nums)):
    #         curr_sum = sum( nums[start:end + 1])
    #         max_sum = max(curr_sum, max_sum)
    # return max_sum
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(maxSubArray([1]) == 1)
print(maxSubArray([5, 4, -1, 7, 8]) == 23)

# [5,  4,-1,7,8]
# max_sum = curr_sum = 5

# curr_sum = max(4, 5 + 4) = 9
# max_sum = max(5, 9) = 9

# curr_sum = max(-1, 9 + (-1)) = 8
# max_sum = max(9, 8) = 9

# curr_sum = max(7, 8 + 7 ) = 15
# max_sum = max(9, 15) = 15

# curr_sum = max(8, 15 + 8) = 23
# max_sum = max(15, 23) = 23
