#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : UnaryCoding.py
# @Author : xxxx
# @Mail   : xxxx@mail.com
# @Date   : 2021/11/22 15:47:00
# @Docs   : 一元码
'''

def UnaryCoding(s):
    '''
    ### Docs: 标准一元码
    ### Args:
        - s: int, 需编码的数
    ### Returns:
        - code: str, 二进制字符串
    '''
    if s == 0:
        code = '0'
    else:
        code = '1' * s + '0'
    return code

def EUik(n=8):
    '''
    ### Docs: 扩展一元码, k增加, 参考 "Generalized Unary Coding"
    ### Args:
        - n: int, 编码需要的位数
    ### Returns:
        - code: dict, 所有数的编码
    '''

    code = {}
    total = (n * (n + 1)) // 2
    i = 0
    c = n # 循环次数, 逐次减少
    k = 0 # 1的个数
    while i <= total and c > 0:
        if i == 0:
            cd = '0' * n
            code[i] = cd
            i = i + 1
        else:
            ci = c - 1
            k += 1
            cd = '0' * (n-k) + '1' * k
            code[i] = cd
            i = i + 1
            while ci > 0:
                cd = cd[1:] + cd[0] # 左移1位
                code[i] = cd
                i = i + 1
                ci = ci - 1
            c = c - 1
    return code

def EUfk(n=8, k=3):
    '''
    ### Docs: 扩展一元码, k固定, 参考 "Generalized Unary Coding"
    ### Args:
        - n: int, 编码需要的位数
        - k: int, 1的个数
    ### Returns:
        - code: dict, 所有数的编码
    '''

    code = {}
    total = (n-k)**2 - 1
    i = 0
    c = n - k - 1 # 循环次数
    s = 0 # 间隔s个置为1
    while i <= total:
        if i == 0:
            cd = '0' * n
            code[i] = cd
            i = i + 1
        else:
            cd = '0' * (n-k) + '1' * k
            if s:
                # 第一个循环, 没有bit需要置为1
                idx = n-(k+s+1)
                cd = cd[0:idx] + '1' + cd[idx+1:]
            code[i] = cd
            i = i + 1
            ci = c
            while ci >= 0:
                cd = cd[1:] + cd[0]
                code[i] = cd
                i = i + 1
                ci = ci - 1
            s = s + 1
    return code

def OEUfk(n=8, k=3):
    '''
    ### Docs: 扩展一元码, k固定, 参考 "Optimization of Generalized Unary Coding"
    ### Args:
        - n: int, 编码需要的位数
        - k: int, 1的个数
    ### Returns:
        - code: dict, 所有数的编码
    '''

    code = {}
    total = n*(n-k-1) + 1
    i = 0
    c = n-1 # 循环次数
    s = 0 # 间隔s个置为1
    while i <= total:
        if i == 0:
            cd = '0' * n
            code[i] = cd
            i = i + 1
        else:
            cd = '0' * (n-k) + '1' * k
            if s:
                # 第一个循环, 没有bit需要置为1
                idx = n-(k+s+1)
                cd = cd[0:idx] + '1' + cd[idx+1:]
            code[i] = cd
            i = i + 1
            ci = c
            while ci > 0 and i <= total:
                cd = cd[1:] + cd[0]
                code[i] = cd
                i = i + 1
                ci = ci - 1
            s = s + 1
    return code


if __name__ == '__main__':

    code1 = {}
    for i in range(10):
        code1[i] = UnaryCoding(i)
    code2 = EUik(n=8)
    code3 = EUfk(n=8,k=3)
    code4 = OEUfk(n=8,k=3)

    # print(len(code1))
    # print(len(code2))
    # print(len(code3))
    # print(len(code4))

    total = max([len(code1), len(code2), len(code3), len(code4)])
    print(total)

    with open('unary_cmp.md', 'w') as fw:
        fw.write('data | UC(10) | EUik(8) | EUfk(8,3) | OEUfk(8,3) \n')
        fw.write(':-: | -: | :-: | :-: | :-: \n')
        for i in range(total):
            uc_cd = '-' if i not in code1 else code1[i]
            EUik_cd = '-' if i not in code2 else code2[i]
            EUfk_cd = '-' if i not in code3 else code3[i]
            OEUfk_cd = '-' if i not in code4 else code4[i]
            fw.write(' %d | %s | %s | %s | %s \n' % (i, uc_cd, EUik_cd, EUfk_cd, OEUfk_cd))
