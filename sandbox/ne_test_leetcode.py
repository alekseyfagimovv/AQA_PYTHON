class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]  
            seen[nums[i]] = i

    # Даны числа и целочисленная цель, 
    # возвращает индексы двух чисел так, чтобы их сумма составляла цель НЕ УСПЕЛ ДОДЕЛАТь

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

isPalindrome = Solution()
    
def test_isPalindrome():
    result_200 = isPalindrome.isPalindrome(200)
    result_303 = isPalindrome.isPalindrome(303)
    assert result_200 is False
    assert result_303 is True

# pytest -v test_leetcode.py::test_isPalindrome
        # если не четное то вычисляем середину (подчёт) 
        # и первую половину учитывая середину сравниваем со второй реверснутой половиной 
        # если ок то труе если нет то нет
    
       
# Given an integer x, return true if x is a palindrome, and false otherwise.


        