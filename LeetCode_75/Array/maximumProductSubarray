# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr_prod_max = curr_prod_min = max_prod = nums[0]
    for num in nums[1:]:
        if num < 0:
            [curr_prod_min, curr_prod_max] = [curr_prod_max, curr_prod_min] 

        curr_prod_max = max(num, num*curr_prod_max)
        curr_prod_min = min(num, num*curr_prod_min)

        max_prod = max(max_prod, curr_prod_max)
        
    return max_prod

print(maxProduct([2,3,-2,4]) == 6)
print(maxProduct([-2,0,-1]) == 0)
        