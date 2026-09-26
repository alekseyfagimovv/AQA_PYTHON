# # Даны числа и целочисленная цель, 
# # возвращает индексы двух чисел так, чтобы их сумма составляла цель
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i in range(len(nums)):
#             compliment = target - nums[i]
#             if compliment in seen:
#                 return [seen[compliment], i]  
#             seen[nums[i]] = i


# # Given an integer x, return true if x is a palindrome, and false otherwise.
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         quantity_numbers = len(x_str)
#         if quantity_numbers % 2 == 0:
#             if x_str[0:quantity_numbers // 2] == x_str[quantity_numbers // 2:][::-1]:
#                 return True
#         else:
#             middle_char = int(x_str[quantity_numbers // 2])
#             if x_str[0:middle_char] == x_str[middle_char:][::-1]:
#                 return True
#         return False
    

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return True if str(x)==str(x)[::-1] else False
    

# MCMXCIV 1994
class Solution: 
    def romanToInt(self, s: str) -> int:
        result = 0
        char = 0
        step = 1
        for first_lett in s:
            print(f'{result} Это текущий результат')
            print(first_lett)
            if char == len(s):
                return result 
            if step < len(s):
                for second_lett in s[step]:
                    print('дошёл 1')
                    print(first_lett, second_lett)
                    if first_lett == 'I' and (second_lett == 'V' or second_lett == 'X'):
                        print(f'{result} Это текущий результат думаем вычесть {second_lett}')
                        result += -2
                    if first_lett == 'X' and (second_lett == 'L' or second_lett == 'C'):
                        result += -20
                    if first_lett == 'C' and (second_lett == 'D' or second_lett == 'M'):
                        result += -200
            # print(f'{len(s) - char} Это Оставшиеся символы')
            # print(f'{char} Это пройденные шаги')
            # Берём по два
            # Если I перед V или X то -1 
            # Если X перед L или C то -10
            # Если C перед D или M то -100
            # Если нет, то берём по 1
            if first_lett == "I":
                print(f'{result} Это текущий результат думаем прибавить')
                result += 1
            if first_lett == "V":
                result += 5
            if first_lett == "X":
                result += 10
            if first_lett == "L":
                result += 50
            if first_lett == "C":
                result += 100
            if first_lett == "D":
                result += 500
            if first_lett == "M":
                result += 1000
            char += 1
            step += 1
        return result
rez = Solution()
solved = rez.romanToInt("MCMXCIV")
print(solved)

# Преобразование римских цифр в обычные
# Пишутся от большей к меньшей слева направо
# Число IIII (4) пишется как IV (4) т.к. единица стоит перед пятеркой мы вычитаем её, получая 4
# Тот же принцип применим к числу IX (9) 
# I можно поставить перед V и X чтобы получилось 4 и 9
# X можно поставить перед L (50) и C (100) чтобы получилось 40 и 90
# C можно поставить перед D (500) чтобы получилось 400 и 900
# Дана римская цифра, преобразуйте её в число

#  РАЗОБРАТЬ РЕШЕНИЕ
class Solution:
  def romanToInt(self, s: str) -> int:
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    for a, b in zip(s, s[1:]):
      if roman[a] < roman[b]:
        ans -= roman[a]
      else:
        ans += roman[a]

    return ans + roman[s[-1]]



