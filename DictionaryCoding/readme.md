# 字典编码

[Dictionary Coder](https://en.wikipedia.org/wiki/Dictionary_coder), 也称之为替代编码器(**Substitution Coder**), 中文称之为**字典编码**(或者词典编码, 这里统一称作字典编码).

## 基本原理

字典编码就是模仿人类查询字典的方法, 用词语在字典中的位置来替代词语. 因而其原理为: 通过匹配算法, 查找要被压缩的文本在一个数据结构(字典)中的匹配位置, 对匹配位置进行表示从而完成编码.

## 发展历程

字典编码最早由 [Abraham Lempel](https://en.wikipedia.org/wiki/Abraham_Lempel) 和 [Jacob Ziv](https://en.wikipedia.org/wiki/Jacob_Ziv) 2位大牛于1977年提出, 后面又出现了各种改进版本, 如下所示:

![dictionary_coder_course](https://gitee.com/yfor1008/pictures/raw/master/dictionary_coder_course.png)

## 分类

从原理可知, 字典编码涉及2个方面的问题: 一是如何构造字典; 二是如何表示查找结果.

根据如何构造字典, 字典编码主要分类2大类: 一是 **LZ77(详见: [LZ77](https://github.com/yfor1008/DataCompress/blob/main/DictionaryCoding/lz77.md))**, 使用滑动窗口来构建字典; 二是 **LZ78(详见: [LZ78](https://github.com/yfor1008/DataCompress/blob/main/DictionaryCoding/lz78.md))**, 使用动态字典来构建字典.

根据如何表示查找结果, 字典编码出现不同的改进, 有了不同字典压缩方法.

## 典型应用

字典编码使用最多的是在文本压缩中, 常见的文本压缩工具, [zip](https://zh.wikipedia.org/wiki/ZIP%E6%A0%BC%E5%BC%8F), [7z](https://zh.wikipedia.org/wiki/7z)等都使用了. 还用图像压缩中, 如[png](https://zh.wikipedia.org/wiki/PNG), [TIFF](https://zh.wikipedia.org/wiki/TIFF). 具体地:

- `zip`: 支持`Deflate`算法
- `7Z`: 支持`LZMA`, `Deflate`算法
- `png`: 使用`Deflate`算法
- `TIFF`: 使用`LZW`算法
