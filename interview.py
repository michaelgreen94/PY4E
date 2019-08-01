from linked_list import linked_list
from linked_list import linkedSolution
# PROBLEM 1
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain
#  a single digit. Add the two numbers and return it as a linked list.


l1 = linked_list()
l1.prefixNode(2)
l1.prefixNode(4)
l1.prefixNode(3)

l2 = linked_list()
l2.prefixNode(5)
l2.prefixNode(6)
l2.prefixNode(4)

result = linkedSolution().addTwoNumbers(l1.head, l2.head)
while result:
    print('linkedSolution - ' + str(result.val))
    result = result.next


# PROBLEM 2
# Given a string, find the length of the longest substring without repeating characters.


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         prev = None
#         start = None
#         count = 0
#         pos = 0
#         found = 0
#         longest = 0
#         while not found:
#             letter = s[pos]
#             if not count:
#                 start = s[pos]
#             count += 1
#             pos += 1
#             if letter != prev:
#                 prev = letter
#             if count and start == letter:

#             if count > longest:
#                 longest = count
#             else:
#                 count = 0
#         return count


# print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# # 10
