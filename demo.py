#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 11:38
# @Author  : dengtf
# @File    : demo.py.py
# from itertools import product
# num_list = ['A','B','C','D','E']
#
# result = product(num_list,repeat=2)
# # for i in num_list:
# # for j in num_list:
# # for k in num_list:
# # if len(set((i,j,k))) == 3:#去重后长度仍为3的话说明i,j,k的值都不相同
# # result.append(list((i,j,k)))
# # list(result)
# print(list(result))

# from itertools import permutations
#
# perm = permutations(['A','B','C','D','E'])
# print(list(perm))
#
# from itertools import combinations
#
# def combine(temp_list, n):
#     '''根据n获得列表中的所有可能组合（n个元素为一组）'''
#     temp_list2 = []
#     for c in combinations(temp_list, n):
#         if c is not None:
#             temp_list2.append(c)
#     return temp_list2
#
# list1 = ['A', 'B', 'C', 'D', 'E']
# end_list = []
# for i in range(len(list1)):
#     end_list.extend(combine(list1, i))
# print(end_list)
# print(len(end_list))

from itertools import combinations

# 待组合的列表
lst = [1,186,3,24,5]

# 生成所有可能的组合
combinations_lst = []
for r in range(1, len(lst) + 1):
    combinations_lst += list(combinations(lst, r))

# 打印所有可能的组合
for combination in combinations_lst:
    print(list(combination))
print(len(combinations_lst))


