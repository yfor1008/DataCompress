#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : ExpGolombCoding.py
# @Author : xxxx
# @Mail   : xxxx@mail.com
# @Date   : 2021/11/25 10:11:19
# @Docs   : exp-golomb 编码
'''

import numpy as np
from UnaryCoding import UnaryCoding
from TruncatedBinaryCoding import int2bin

def ExpGolombEncoding(x, k=0):
    '''
    ### Docs: exp-golomb 编码, 参考: https://www.cnblogs.com/wangguchangqing/p/6297792.html
    ### Args:
        - x: int, 待编码的数
        - k: int, 
    ### Returns:
        - code: str, 二进制字符串
    '''

    m = int(np.floor(np.log2(x//(2**k)+1)))
    offset = x - (2**m - 1) * 2**k
    bins = int2bin(offset, m+k)

    code = '0'*m + '1' + bins
    return code

def ExpGolombDecoding(bins, k=0):
    '''
    ### Docs: exp-golomb 解码, 参考: https://www.cnblogs.com/wangguchangqing/p/6297792.html
    ### Args:
        - bins: str, 编码后的二进制字符串
        - k: int, 
    ### Returns:
        - datas: list, 解码后的数据
    '''

    m = 0
    cur = 0
    data = []
    while cur < len(bins):
        if int(bins[cur], 2) == 1:
            if m == 0:
                offset = int(bins[cur+1:cur+1+m+k], 2)
                d = 2**k * (2**m - 1) + offset
                data.append(d)
                cur = cur + 1 + m + k
            else:
                offset = int(bins[cur+1:cur+1+m+k], 2)
                d = 2**k * (2**m - 1) + offset
                data.append(d)
                cur = cur + 1 + m + k
                m = 0
        else:
            # =1, 继续一元码解码
            m = m + 1
            cur = cur + 1
    return data

if __name__ == '__main__':

    # # test1
    # data_num = 30
    # k_num = 4
    # codes = {}

    # for k in range(k_num):
    #     cd_k = {}
    #     for x in range(data_num):
    #         cd = ExpGolombEncoding(x, k)
    #         cd_k[x] = cd
    #     codes[k] = cd_k
    # # print(codes[3])

    # with open('exp_cmp.md', 'w') as fw:
    #     fw.write(' x | k=0 | k=1 | k=2 | k=3 \n')
    #     fw.write(' :-: | :-: | :-: | :-: | :-: \n')
    #     for x in range(data_num):
    #         cds = [str(x)]
    #         for k in range(k_num):
    #             m = int(np.floor(np.log2(x//(2**k)+1)))
    #             cd = codes[k][x]
    #             idx = len(cd) - (m+k)
    #             cd = cd[:idx] + '\|' + cd[idx:]
    #             cds.append(cd)
    #         cds = '|'.join(cds)
    #         fw.write(' %s \n' % cds)

    # test2
    datas = [5, 0, 7, 9, 8, 4, 1, 2, 3, 7, 2, 1, 6, 0]
    k = 1
    codes = ''
    for d in datas:
        code = ExpGolombEncoding(d, k)
        codes += code
    print(codes)

    datas1 = ExpGolombDecoding(codes, k)
    print(datas1)

    print(datas == datas1)
