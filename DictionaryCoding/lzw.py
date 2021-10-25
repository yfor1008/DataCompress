#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

class LZW:
    '''
    LZW 算法实现, 仅支持字母及数字组成的字符串, 因为初始字典必须包含所有可能的单个字符
    '''

    def __init__(self) -> None:
        # 由字母和数字构成初始字典
        self.dicts = list(string.ascii_letters + string.digits)
        self.indexs = list(range(len(self.dicts)))

    def encode(self, data, show=False):
        '''
        ### Docs: 编码
            - 原理:
                - 查找最长匹配字符串 S
                - 输出(index): 在字典中匹配的 index
                - 将 Sc 添加到字典中, c 为下一个字符
            ### Args:
            - data: string, 待处理数据, 由数字和字母组成
            - show: bool, 是否显示中间结果
        ### Returns:
            - compressed: list, 压缩后数据, [index0, index1, ...]
        '''

        compressed = []

        current = 0
        dict_index = len(self.dicts) - 1
        data_len = len(data)
        while current < data_len:

            # 查找最长匹配
            for j in range(current+1, data_len+1):
                words = data[current:j]
                if words not in self.dicts:
                    cmp = self.dicts.index(data[current:j-1])
                    dict_index += 1
                    self.dicts.append(words)
                    self.indexs.append(dict_index)

                    current = j - 1
                    break
                elif j == data_len:
                    # 最后一个字符
                    cmp = self.dicts.index(data[current:j])
                    current = j

            if show:
                print(cmp, self.dicts, self.indexs)
            compressed.append(cmp)
        return compressed

    def decode(self, compressed, show=False):
        '''
        ### Docs: 解码
        ### Args:
            - compressed: list, 压缩后数据, [index0, index1, ...]
            - show: bool, 是否显示中间结果
        ### Returns:
            - data: string, 解码后数据
        '''

        dict_index = len(self.dicts)
        data = ''

        for index in compressed:
            idx = self.indexs.index(index)
            words = self.dicts[idx]
            data += words

            if show:
                print(data)

        return data

if __name__ == '__main__':

    import random

    def random_strings():
        '''随机生成字符串'''
        length = random.randint(20, 200)
        strings = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return strings

    compressor = LZW()

    # data = 'aabaacabcabcb'
    data = random_strings()
    compressed = compressor.encode(data)
    data1 = compressor.decode(compressed)
    print(data)
    print(compressed)
    print(data1)
    print(data == data1)
