# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique_nums = set(nums)
    is_contains_dubl = False if len(unique_nums) == len(nums) else True
    return is_contains_dubl


print(containsDuplicate([1, 2, 3, 1]) == True)
print(containsDuplicate([1, 2, 3, 4]) == False)
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
