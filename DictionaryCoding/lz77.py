#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LZ77:
    '''
    LZ77 算法实现
    '''

    def __init__(self, window_size=20, lookahead_buffer_size=4):
        max_window_size = 100
        self.window_size = min(window_size, max_window_size)
        self.lookahead_buffer_size = lookahead_buffer_size

    def find_longest_match(self, data, current):
        '''
        ### Docs: 查找最长匹配串
        ### Args:
            - data: list, 待处理数据
            - current: int, 当前处理数据index
        '''

        buffer_end = min(current + self.lookahead_buffer_size, len(data))
        position = 0
        length = 0

        for j in range(current+1, buffer_end+1):
            # lookahead buffer 中待编码的子串, 子串长度会不断增加, 直到匹配最大长度
            substring = data[current:j]

            # 在字典中查找匹配字符串, 遍历字典中所有可能的位置,
            start_index = max(0, current - self.window_size) # 字典区域起始位置
            for i in range(start_index, current):
                # current-i 为起始查找位置到字典结束位置的长度, 即实际字典的长度
                # 如果待编码字符串长度>实际字典长度, 则将字典进行循环扩展
                dict_len = current - i
                repetitions = len(substring) // dict_len # 重复扩展次数
                last = len(substring) % dict_len

                # 扩展后的字典
                matched_string = data[i:current] * repetitions + data[i:i+last]

                if matched_string == substring and len(substring) > length:
                    # 最大匹配
                    position = dict_len
                    length = len(substring)

        return (position, length)

    def encode(self, data):
        '''
        ### Docs: 编码
        ### Args:
            - data: string, 待处理数据
        ### Returns:
            - compressed: list, 压缩后数据, [(p,l,c), (p,l,c), ...]
        '''

        compressed = []
        current = 0
        while current < len(data):

            match = self.find_longest_match(data, current)
            (position, length) = match

            current += length + 1

            if current > len(data):
                char = ''
            else:
                char = data[current-1]
            
            compressed.append((position, length, char))
        return compressed

    def decode(self, compressed):
        '''
        ### Docs: 解码
        ### Args:
            - compressed: list, 压缩后数据, [(p,l,c), (p,l,c), ...]
        ### Returns:
            - data: string, 解码后数据
        '''

        data = ''
        current = 0

        for (position, length, char) in compressed:
            if position >= length:
                # 字典比匹配数据长
                data += data[current-position:current-position+length]
            elif position < length:
                # 字典比匹配数据短, 需进行扩展
                repetitions = length // position # 重复扩展次数
                last = length % position
                data += data[current-position:current]*repetitions
                data += data[current-position:last]
            if char:
                # 如果 char 为空, 则为最后数据最后
                data += char
            current += length + 1

        return data

if __name__ == '__main__':

    import random
    import string

    def random_strings():
        '''随机生成字符串'''
        length = random.randint(20, 200)
        strings = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        return strings

    compressor = LZ77(window_size=6)

    # data = 'aacaacabcabaaac'
    data = random_strings()
    compressed = compressor.encode(data)
    data1 = compressor.decode(compressed)
    print(data)
    # print(compressed)
    print(data1)
    print(data == data1)
