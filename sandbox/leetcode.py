class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]  
            seen[nums[i]] = i

    # Даны числа и целочисленная цель, 
    # возвращает индексы двух чисел так, чтобы их сумма составляла цель