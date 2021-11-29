## 哈夫曼编码

[哈夫曼编码](https://zh.wikipedia.org/wiki/%E9%9C%8D%E5%A4%AB%E6%9B%BC%E7%BC%96%E7%A0%81)是一种无损压缩方法, 由 [David A. Huffman](https://zh.wikipedia.org/wiki/%E5%A4%A7%E8%A1%9B%C2%B7%E9%9C%8D%E5%A4%AB%E6%9B%BC) 于1952年在麻省理工学院读博士期间提出的, 该算法是依据信源符号出现的概率来构造码字, 发表于["A Method for the Construction of Minimum-Redundancy Codes"](https://web.archive.org/web/20050530145744/http://compression.graphicon.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf).

### 原理

基本原理可以概括为:
- 对出现次数多的数据分配较短的码字
- 对出现次数少的数据分配较长的码字

这样使得所有数据平均码长更小.

如下图所示示例, 不断对数据进行排序合并, 直到所有数据处理完, 这样就可以根据路径得到每个数据的编码.

![huffmanCoding](https://gitee.com/yfor1008/pictures/raw/master/huffmanCoding.png)

哈夫曼编码是一种前缀编码, 解码时与码字进行匹配即可以得到解码后的数据.

## 范式哈夫曼编码

哈夫曼编码可能存在多种情况, 如下图所示的2种情况都是最优的, 因而需要存储较多的数据才能完成解码工作.

![huffmanTreeCmp](https://gitee.com/yfor1008/pictures/raw/master/huffmanTreeCmp.png)

针对这个问题, 提出了范式哈夫曼编码.

[范式哈夫曼编码(Canonical Huffman Code)](https://zh.wikipedia.org/wiki/%E8%8C%83%E6%B0%8F%E9%9C%8D%E5%A4%AB%E6%9B%BC%E7%B7%A8%E7%A2%BC)是哈夫曼编码的一种特殊情况, 对哈夫曼编码进行了约束, 从而可以减少需要的存储空间及查找复杂度, 因而实际使用中, 基本都是使用范式哈夫曼编码.

### 约束/规则

总结起来有以下3个规则:

1. 最小编码长度的第一个编码必须从`0`开始
2. 相同长度的编码必须是连续的
3. 编码长度为`j`的第一个编码由编码长度为`j-1`的最后一个编码得到, 即 $c_j=2*(c_{j-1}+1)$ , 这个公式的意思是, 编码长度为`j-1`的最后一个编加上`1`后, 左移一位

使用上述规则可很容易生成哈夫曼表, 而只需要存储需要编码的数据(按概率从高到底排列)即对应的码长就可以了.

### 实际应用

最常见的应该就是JPEG压缩算法了, 这里以JPEG中的DHT为例进行说明.

JPEG中的DHT进一步进行了优化, 使用了行程编码对每个数据需要的bit数进行了压缩. 如下图所示:

![generate_huffman_table](https://gitee.com/yfor1008/pictures/raw/master/generate_huffman_table.png)
