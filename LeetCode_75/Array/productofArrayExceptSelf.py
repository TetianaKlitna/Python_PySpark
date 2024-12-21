# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    size = len(nums)
    answer = [1]*size
    prod = 1
    for i in range(size):
        answer[i] = prod
        prod *= nums[i]

    prod = 1
    for i in range(size - 1, -1, -1):
        answer[i] *= prod
        prod *= nums[i]

    return answer
    # 1| 2* 3* 4*
    # 1* 2| 3* 4*
    # 1* 2* 3| 4*
    # 1* 2* 3* 4|


print(productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
