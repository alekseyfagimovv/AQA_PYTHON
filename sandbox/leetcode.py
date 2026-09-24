# Даны числа и целочисленная цель, 
# возвращает индексы двух чисел так, чтобы их сумма составляла цель
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]  
            seen[nums[i]] = i


# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        quantity_numbers = len(x_str)
        if quantity_numbers % 2 == 0:
            if x_str[0:quantity_numbers // 2] == x_str[quantity_numbers // 2:][::-1]:
                return True
        else:
            middle_char = int(x_str[quantity_numbers // 2])
            if x_str[0:middle_char] == x_str[middle_char:][::-1]:
                return True
        return False
    

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False





