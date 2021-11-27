#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : GolombCoding.py
# @Author : xxxx
# @Mail   : xxxx@mail.com
# @Date   : 2021/11/23 15:19:22
# @Docs   : golomb 编码
'''

import numpy as np
from UnaryCoding import UnaryCoding
from TruncatedBinaryCoding import TruncatedBinaryEncoding

def GolombEnCoding(x, m=8):
    '''
    ### Docs: golomb 编码, 当m为2的幂次时, 为 golomb-rice 编码, 参考: https://zhuanlan.zhihu.com/p/180520059
    ### Args:
        - x: int, 待编码的数
        - m: int, 分组长度
    ### Returns:
        - code: str, 二进制字符串
    '''

    q = x // m
    r = x % m

    cd_q = UnaryCoding(q)
    cd_r = TruncatedBinaryEncoding(r, m)

    code = cd_q + cd_r

    return code, cd_q, cd_r

def GolombDeCoding(bins, m=8):
    '''
    ### Docs: golomb 解码, 当m为2的幂次时, 为 golomb-rice 编码, 参考: https://zhuanlan.zhihu.com/p/180520059
    ### Args:
        - bins: str, 编码后的二进制字符串
        - n: int, 数据种类的个数
    ### Returns:
        - datas: list, 解码后的数据
    '''

    k1 = int(np.floor(np.log2(m)))
    k2 = int(np.ceil(np.log2(m)))
    u = 2 ** (k1+1) - m

    cur = 0
    cnt = 0
    data = []
    while cur < len(bins):
        if int(bins[cur], 2) == 0:
            if cnt == 0:
                # 商q=0
                cd_q = 0
                cd_r = int(bins[cur+1:cur+1+k1], 2)
                d = cd_q * m + cd_r
                data.append(d)
                cur = cur + 1 + k1
            else:
                cd_q = cnt
                cd_r = int(bins[cur+1:cur+1+k1], 2)
                if cd_r < u:
                    # 前u个数使用k1个bit
                    d = cd_q * m + cd_r
                    data.append(d)
                    cur = cur + 1 + k1
                else:
                    # 后n-u个数使用k2个bit
                    cd_r = int(bins[cur+1:cur+1+k2], 2)
                    d = cd_q * m + cd_r
                    data.append(d)
                    cur = cur + 1 + k2
                cnt = 0
        else:
            # =1, 继续一元码解码
            cnt = cnt + 1
            cur = cur + 1

    return data

if __name__ == '__main__':

    # # test1
    # num = 11
    # codes1 = {}
    # cd_q1 = {}
    # cd_r1 = {}
    # m = 3
    # for i in range(num):
    #     code, cd_q, cd_r = GolombEnCoding(i, m)
    #     codes1[i] = code
    #     cd_q1[i] = cd_q
    #     cd_r1[i] = cd_r
    # print(codes1)

    # codes2 = {}
    # cd_q2 = {}
    # cd_r2 = {}
    # m = 4
    # for i in range(num):
    #     code, cd_q, cd_r = GolombEnCoding(i, m)
    #     codes2[i] = code
    #     cd_q2[i] = cd_q
    #     cd_r2[i] = cd_r
    # # print(codes2)

    # codes3 = {}
    # cd_q3 = {}
    # cd_r3 = {}
    # m = 5
    # for i in range(num):
    #     code, cd_q, cd_r = GolombEnCoding(i, m)
    #     codes3[i] = code
    #     cd_q3[i] = cd_q
    #     cd_r3[i] = cd_r
    # # print(codes3)

    # codes4 = {}
    # cd_q4 = {}
    # cd_r4 = {}
    # m = 8
    # for i in range(num):
    #     code, cd_q, cd_r = GolombEnCoding(i, m)
    #     codes4[i] = code
    #     cd_q4[i] = cd_q
    #     cd_r4[i] = cd_r
    # # print(codes4)

    # title_str = [str(i) for i in range(num)]
    # title_str = '|'.join(title_str)
    # title_str = 'n|' + title_str
    # seg_str = [':-:'] * (num+1)
    # seg_str = '|'.join(seg_str)
    # m3_str = [cd_q1[i] + '\|' + cd_r1[i] for i in range(num)]
    # m3_str = '|'.join(m3_str)
    # m3_str = 'm=3|' + m3_str
    # m4_str = [cd_q2[i] + '\|' + cd_r2[i] for i in range(num)]
    # m4_str = '|'.join(m4_str)
    # m4_str = 'm=4|' + m4_str
    # m5_str = [cd_q3[i] + '\|' + cd_r3[i] for i in range(num)]
    # m5_str = '|'.join(m5_str)
    # m5_str = 'm=5|' + m5_str
    # m8_str = [cd_q4[i] + '\|' + cd_r4[i] for i in range(num)]
    # m8_str = '|'.join(m8_str)
    # m8_str = 'm=8|' + m8_str

    # with open('golomb_cmp.md', 'w') as fw:
    #     fw.write('%s \n' % title_str)
    #     fw.write('%s \n' % seg_str)
    #     fw.write('%s \n' % m3_str)
    #     fw.write('%s \n' % m4_str)
    #     fw.write('%s \n' % m5_str)
    #     fw.write('%s \n' % m8_str)


    # test2
    m = 8
    datas = [5, 4, 8, 5, 7, 9, 3, 7, 2, 1, 6]
    codes = ''
    for d in datas:
        code,_,_ = GolombEnCoding(d, m)
        codes += code
    print(codes)

    datas1 = GolombDeCoding(codes, m)
    print(datas1)

    print(datas == datas1)
