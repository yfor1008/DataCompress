#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : TruncatedBinaryCoding.py
# @Author : xxxx
# @Mail   : xxxx@mail.com
# @Date   : 2021/11/23 13:57:36
# @Docs   : 截断二进制编码
'''

import numpy as np

def int2bin(n, count=24):  
    '''returns the binary of integer n, using count number of digits''' 
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)]) 

def TruncatedBinaryEncoding(x, n):
    '''
    ### Docs: 截断二进制编码
    ### Args:
        - x: int, 待编码的数, 0<=x<n
        - n: int, 需编码数据的个数
    ### Returns:
        - code: str, 二进制字符串
    '''

    k1 = int(np.floor(np.log2(n)))
    k2 = int(np.ceil(np.log2(n)))
    u = 2 ** (k1+1) - n

    if x < u:
        code = int2bin(x, k1)
    else:
        code = int2bin(x+u, k2)

    return code

def TruncatedBinaryDecoding(bins, n):
    '''
    ### Docs: 截断二进制解码
    ### Args:
        - bins: str, 编码后的二进制字符串
        - n: int, 数据种类的个数
    ### Returns:
        - data: list, 解码后的数据
    '''

    k1 = int(np.floor(np.log2(n)))
    k2 = int(np.ceil(np.log2(n)))
    u = 2 ** (k1+1) - n

    data = []

    pre = 0
    cur = k1
    while pre < len(bins):
        cur_bin = bins[pre:cur]
        cur_data = int(cur_bin, 2)
        if cur_data < u:
            data.append(cur_data)
        else:
            cur = cur - k1 + k2
            cur_bin = bins[pre:cur]
            cur_data = int(cur_bin, 2) - u
            data.append(cur_data)
        pre = cur
        cur = cur + k1

    return data

if __name__ == '__main__':

    # # test1
    # num = 10
    # code1 = {}
    # for i in range(num):
    #     cd = TruncatedBinaryEncoding(i, num)
    #     code1[i] = cd
    # # print(code1)

    # code2 = {}
    # for i in range(num):
    #     code2[i] = int2bin(i, 4)
    # # print(code2)

    # k1 = int(np.floor(np.log2(num)))
    # k2 = int(np.ceil(np.log2(num)))
    # u = 2 ** (k1+1) - num

    # with open('tbe_cmp.md', 'w') as fw:
    #     fw.write('data | index | offset | offset value | Standard Binary | Truncated Binary \n')
    #     fw.write(' :-: | :-: | :-: | :-: | :-: | :-: \n')
    #     for i in range(num):
    #         data = 's%d' % i
    #         if i < u:
    #             offset = 0
    #         else:
    #             offset = u
    #         offset_value = i + offset
    #         s_cd = '-' if i not in code2 else code2[i]
    #         t_cd = '-' if i not in code1 else code1[i]
    #         if i < u:
    #             fw.write(' %s | %d | %d | %d | %s | %s \n' % (data, i, offset, offset_value, '~~'+s_cd[0]+'~~'+s_cd[1:], t_cd))
    #         else:
    #             fw.write(' **%s** | **%d** | **%d** | **%d** | **%s** | **%s** \n' % (data, i, offset, offset_value, s_cd, t_cd))


    # test2
    num = 10
    datas = [5, 4, 8, 9, 3, 7, 2, 1, 6]
    codes = ''
    for d in datas:
        code = TruncatedBinaryEncoding(d, num)
        codes += code
    print(codes)

    datas1 = TruncatedBinaryDecoding(codes, num)
    print(datas1)

    print(datas == datas1)
