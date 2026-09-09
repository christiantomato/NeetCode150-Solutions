"""
1. Product of Array Except Self
09/09/26

Approach:
Used hint for prefix and suffix products - used 2 separate loops to compute and one array to store.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #init an array which we will use for both prefix and suffix products
        product_array = [1] * len(nums)

        #compute the prefix product array
        prefix_product = 1
        for i in range(0, len(nums)):
            product_array[i] = prefix_product
            prefix_product *= nums[i]

        #compute suffix products which will result in product except self array
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            product_array[i] *= suffix_product
            suffix_product *= nums[i]

        return product_array
        