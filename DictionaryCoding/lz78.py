#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LZ78:
    '''
    LZ78 算法实现
    '''

    def encode(self, data, show=False):
        '''
        ### Docs: 编码
            - 原理:
                - 查找最长匹配字符串 S
                - 输出(index, c): 在字典中匹配的 index, 和下一个字符 c
                - 将 Sc 添加到字典中
            - 对于匹配结果, 有三种情况:
                - case1: 当前字符不在字典中, 输出(0, c), 将 c 添加到字典中
                - case2: 当前字符在字典中, 且为最后一个字符, 输出(index, '')
                - case3: 当前字符在字典中, 且不为最后一个字符, 查找最长匹配字符串 S, 输出(index, c), 将 Sc 添加到字典中
        ### Args:
            - data: string, 待处理数据
            - show: bool, 是否显示中间结果
        ### Returns:
            - compressed: list, 压缩后数据, [(index0,c0), (index1,c1), ...]
        '''

        dicts = []
        indexs = []
        compressed = []

        current = 0
        dict_index = 0
        data_len = len(data)
        while current < data_len:

            if data[current] not in dicts:
                # case1
                cmp = (0, data[current])
                dict_index += 1
                dicts.append(data[current])
                indexs.append(dict_index)
                current += 1
            elif current == data_len-1:
                # case2
                cmp = (indexs[dicts.index(data[current])], '')
                current += 1
            else:
                # case3
                for j in range(current+1, data_len):
                    # 不断增加字符长度, 直到出现不匹配
                    if data[current:j+1] not in dicts:
                        # case1
                        cmp = (indexs[dicts.index(data[current:j])], data[j])
                        dict_index += 1
                        dicts.append(data[current:j+1])
                        indexs.append(dict_index)
                        current = j + 1
                        break
                    elif j == data_len-1:
                        # case2
                        cmp = (indexs[dicts.index(data[current:j+1])], '')
                        current = j + 1
            if show:
                print(cmp, dicts, indexs)
            compressed.append(cmp)
        return compressed

    def decode(self, compressed, show=False):
        '''
        ### Docs: 解码
        ### Args:
            - compressed: list, 压缩后数据, [(index0,c0), (index1,c1), ...]
            - show: bool, 是否显示中间结果
        ### Returns:
            - data: string, 解码后数据
        '''

        dicts = []
        indexs = []
        dict_index = 0
        data = ''

        for index, char in compressed:
            if index == 0:
                data += char
                dict_index += 1
                dicts.append(char)
                indexs.append(dict_index)
            else:
                idx = indexs.index(index)
                words = dicts[idx]
                data += words+char
                dict_index += 1
                dicts.append(words+char)
                indexs.append(dict_index)

            if show:
                print(data, dicts, indexs)

        return data

if __name__ == '__main__':

    import random
    import string

    def random_strings():
        '''随机生成字符串'''
        length = random.randint(20, 200)
        strings = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return strings

    compressor = LZ78()

    # data = 'aabaacabcabcb'
    data = random_strings()
    compressed = compressor.encode(data)
    data1 = compressor.decode(compressed)
    print(data)
    # print(compressed)
    print(data1)
    print(data == data1)
