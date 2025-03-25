#two sun
from itertools import count
from typing import List


#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

# palindrome number

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#
#         return str(x) == str(x)[::-1]

# longest comon prefix
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         min_length = min(strs, key=len)
#         for i in range(len(min_length)):
#             current_chair = min_length[i]
#             for string in strs:
#                 if string[i] != current_chair:
#                     return min_length[i]
#         return min_length

#valid parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:
#         bracket_map = {')': '(', '}': '{', ']': '['}
#         stack = []
#
#         for char in s:
#             if char in bracket_map:
#                 top_element = stack.pop() if stack else '#'
#                 if bracket_map[char] != top_element:
#                     return False
#             else:
#                 stack.append(char)
#         return not stack


# # start leetcode 75 challenge
#
#1
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         u, k = 0, 0
#         while u < len(word1) and k < len(word2):
#             result.append(word1[u])
#             result.append(word2[k])
#             u += 1
#             k += 1
#         result.extend(word1[u::])
#         result.extend(word2[k::])
#         return ''.join(result)

# #2
# import math
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 +str1:
#             return ""
#         gcd_length = math.gcd(len(str1), len(str2))
#
#         return str1[:gcd_length]

#3
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         max_candies = max(candies)
#         result = []
#         for i in candies:
#             result.append(extraCandies + i >= max_candies)
#         return result

#4

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         length = len(flowerbed)
#         for i in range(length):
#             if flowerbed[i] == 0:
#                 left_empty = i == 0 or flowerbed[i - 1] == 0
#                 right_empty = i == length - 1 or flowerbed[i + 1] == 0
#                 if left_empty and right_empty:
#                     flowerbed[i] = 1
#                     n-=1
#                 if n == 0:
#                     return True
#         return n<=0



#5
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         s=list(s)
#         n=len(s)
#         left=0
#         right=n-1
#         vowels=set('AEIOUaeiou')
#         while left<right:
#             while left<right and s[left] not in vowels:
#                 left+=1
#             while left<right and s[right] not in vowels:
#                 right-=1
#             s[left], s[right]=s[right], s[left]
#             left+=1
#             right-=1
#         s=''.join(s)
#         return s

#6
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(reversed(s.split()))

#7
# class Solution(object):
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         prefix = 1
#         postfix = 1
#         output = [1] * n
#         for i in range(n):
#             output[i] = prefix
#             prefix *= nums[i]
#         for i in range(n - 1, -1, -1):
#             output[i] *= postfix
#             postfix *= nums[i]
#         return output

#8
# class Solution:
#     def increasingTriplet(self, nums):
#         first = float('inf')
#         second = float('inf')
#         for n in nums:
#             if n <= first:
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False

#9
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         i = 0
#         res = []
#
#         while i < len(chars):
#             char = chars[i]
#             count = 1
#
#             while i + 1 < len(chars) and chars[i + 1] == char:
#                 count += 1
#                 i += 1
#
#             res.append(char)
#
#             if count > 1:
#                 res.extend(list(str(count)))
#
#             i += 1
#         chars[:len(res)] = res
#         return len(res)

#10
# Короче я начинаю с начала вот эту 75
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         u, k = 0, 0
#         while u < len(word1) and k < len(word2):
#             result.append(word1[u])
#             result.append(word2[k])
#             u += 1
#             k += 1
#         result.extend(word1[u::])
#         result.extend(word2[k::])
#         return ''.join(result)

#1
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         a, b = 0, 0
#         while a < len(word1) and b < len(word2):
#             result.append(word1[a])
#             result.append(word2[b])
#             a += 1
#             b += 1
#         result.extend(word1[a::])
#         result.extend(word2[b::])
#         return ''.join(result)

#2
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         result = []
#         a = len(str1)
#         b = len(str2)
#         if a > b:
#             c = a-b
#             print(str1[-c:])
#         if b > a:
#             c = b-a
#             print(str1[-c:])
#         else:
#             return ""

# from math import gcd
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 + str1:
#             return ""
#         gcd_ = gcd(len(str1), len(str2))
#         return str1[:gcd_]




























