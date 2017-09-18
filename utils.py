# -*- coding: utf-8 -*-


"""
    implemented eliminate-common-left-factor algorithm
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                (ε)
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: utils.py
@time: 2017/9/8 9:02 
"""

import copy
from collections import defaultdict

# G = {'A': ['abc', 'ab', 'abcd', 'a', 'b', 'bc', 'B']}
# G['B'] = ['Ab', 'Ac']
# print(G)
VN_dict = defaultdict(int)
G_c = None
result = dict()


def eliminate_common_factor(VN, exp_list):
    # G:  {'A': ['abc', 'ab', 'abcd', 'a', 'b', 'bc', 'B']}
    index_dict = get_common_factor(exp_list)
    if have_common_factor(index_dict):
        for k, v in index_dict.items():
            len_k = len(k)
            tmp_list = []
            if len(v) != 1:
                for i in v:
                    exp = exp_list[i][len_k:]
                    tmp_list.append(exp if exp else 'ε')
                new_VN = generate_VN(VN)
                exp_list.append(k + new_VN)  # 加入aA'
                G_c[new_VN] = tmp_list  # 将新生成的规则添加进G_c文法中
    remove_exp(index_dict, exp_list)
    # print('VN:', VN)
    result[VN] = exp_list
    # print('result:', result)
    G_c.pop(VN)


def remove_exp(index_dict, exp_list):
    l = []
    for v in index_dict.values():
        if len(v) != 1:
            l.extend(v)
    # 在对一个list进行pop操作时，必须是按逆序来删除。
    # 即，先删下标大的元素，再删下标小的元素，否则 会越界。
    l = sorted(l, reverse=True)
    for index in l:
        exp_list.pop(index)


def get_common_factor_aux(exp_list):
    """
    对于 G = {'A': 'abc ab abcd a b bc'}
    :param exp_list: 文法G中每条产生式右部的集和的列表形式：['abc', 'ab', 'abcd', 'a', 'b', 'bc']
    :return: 类型为字典，key为首字符，value为所在index：{'b': [4, 5], 'a': [0, 1, 2, 3]})
    """
    d = defaultdict(list)
    for index, exp in enumerate(exp_list):
        d[exp[0]].append(index)
    return d


def get_common_factor(exp_list):
    d = get_common_factor_aux(exp_list)
    index = 1
    d_copy = copy.deepcopy(d)
    for k, v in d.items():
        new_k = copy.deepcopy(k)
        k_copy = copy.deepcopy(k)
        while True:
            try:
                c = exp_list[v[0]][index]
            except Exception as e:
                break
            for i in v:
                try:
                    char = exp_list[i][index]
                except:
                    break
                if char == c:
                    pass
                else:
                    break
            else:
                new_k = k_copy + c
                d_copy[new_k] = v
                del d_copy[k_copy]
                index += 1
                k_copy = copy.deepcopy(new_k)
                continue
            if new_k == k_copy:
                break
    return d_copy


def have_common_factor(d):
    for v in d.values():
        if len(v) != 1:
            return True
    else:
        return False


def generate_VN(VN):
    VN_dict[VN[0]] += 1
    return VN[0] + VN_dict[VN[0]] * "'"


def wise(G):
    global G_c, VN_dict, result
    VN_dict = defaultdict(int)
    G_c = copy.deepcopy(G)
    result = dict()
    while True:
        size = len(result)
        try:
            for k, v in G.items():
                eliminate_common_factor(k, v)
        except Exception as e:
            raise e
        G = copy.deepcopy(G_c)
        if size == len(result):
            break
    return result


if __name__ == '__main__':
    G = {'A': ['abc', 'ab', 'abcd', 'a', 'b', 'bc', 'B']}
    G_c = copy.deepcopy(G)
    while True:
        size = len(result)
        try:
            for k, v in G.items():
                eliminate_common_factor(k, v)
        except Exception as e:
            raise e
        G = copy.deepcopy(G_c)
        if size == len(result):
            break
    print(result)
