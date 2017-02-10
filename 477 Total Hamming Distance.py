class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_hamming_distance = 0
        length = len(nums)

        for i in range(1, 31):
            bit_count_of_1 = 0
            for j in range(len(nums)):
                if (nums[j] >> 1) << 1 != nums[j]:
                    bit_count_of_1 += 1
                nums[j] = nums[j] >> 1
            total_hamming_distance += bit_count_of_1 * (length - bit_count_of_1)
        return total_hamming_distance