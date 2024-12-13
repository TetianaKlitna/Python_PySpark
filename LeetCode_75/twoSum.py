# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(nums, target):
    dict_nums = {}
    for curr_ind, curr_num in enumerate(nums):
        dict_nums[curr_num] = dict_nums.get(curr_num, []) + [curr_ind]
        # print(dict_nums)
        search_num = target - curr_num
        search_ind = dict_nums.get(search_num, [])
        if search_ind != []:
            for ind in search_ind:
                if ind != curr_ind:
                    return [ind, curr_ind]


print(twoSum([2, 7, 11, 15], 9) == [0, 1])
print(twoSum([3, 2, 4], 6) == [1, 2])
print(twoSum([3, 3], 6) == [0, 1])
