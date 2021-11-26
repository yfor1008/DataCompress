# 一元码

**一元码([Unary Coding](https://en.wikipedia.org/wiki/Unary_coding))**

是一种前缀编码, 其编码规则是: 
对非负整数`n`, 可以表示为`n`或`n-1`个`1`后面跟一个`0`, `1`和`0`可以互换. 它对几何分布的数据编码最优.

**广义一元码([Generalized Unary Coding, 2016](https://doi.org/10.1007%2Fs00034-015-0120-7))**

对标准一元码进行扩展, 扩展后使用固定位数的bit来对数据进行编码, 扩展后的一元码有2个参数(n,k):
- `n`: 每个数据编码需要的bit位数
- `k`: 编码种使用1的位数

针对`k`的不同, 有2种扩展方式:
- k增加: `n`个bit最大可以编码`n(n+1)/2`个数, 称为`EUik(Extended Unary, increasing k)`
- k固定: `n`个bit最大可以编码`(n-k)^2-1`个数, 称为`EUfk(Extended Unary, fixed k)`

**改进的广义一元码([Optimization of Generalized Unary Coding, 2016](https://arxiv.org/ftp/arxiv/papers/1611/1611.03353.pdf))**

对`EUfk`进行了改进, `n`个bit最大可以编码`n(n-k-1)+1`个数, 称为`OEUfk(Optimized Extending Unary, fixed k)`.

**原理及区别**

对于这几种改进方式, 其基本原理都是分组+位移来实现, 如下图所示, 只不过分组`Ci`的大小`Li`及位移的方式不同而已.

- 对于`EUik`: `m=n-1`, `Ci`的长度`Li`从`n`开始依次递减, 对于每个分组, 初始编码都为`n-k个0+k个1`, 执行`Li`次左移1位操作形成每个分组的编码, 对所有分组执行该操作得到所有数据编码;
- 对于`EUfk`: `m=n-k-1`, `Ci`的长度`Li`恒定为`n-k+1`, 对于每个分组, 初始编码都为`n-k个0+k个1`, 当`i>1`时, 初始编码的第`n-(k+i+1)`位需置为1,  执行`Li`次左移1位操作形成每个分组的编码, 对所有分组执行该操作得到所有数据编码;
- 对于`OEUfk`: `m=n-k-1`, `Ci`的长度`Li`恒定为`n-1`, 对于每个分组, 初始编码都为`n-k个0+k个1`, 当`i>1`时, 初始编码的第`n-(k+i+1)`位需置为1,  执行`Li`次左移1位操作形成每个分组的编码, 对所有分组执行该操作得到所有数据编码;

![unary_coding](https://gitee.com/yfor1008/pictures/raw/master/unary_coding.png)

**编码示例**

| data |      UC(10) | EUik(8)  | EUfk(8,3) | OEUfk(8,3) |
| :--: | ----------: | :------: | :-------: | :--------: |
|  0   |           0 | 00000000 | 00000000  |  00000000  |
|  1   |          10 | 00000001 | 00000111  |  00000111  |
|  2   |         110 | 00000010 | 00001110  |  00001110  |
|  3   |        1110 | 00000100 | 00011100  |  00011100  |
|  4   |       11110 | 00001000 | 00111000  |  00111000  |
|  5   |      111110 | 00010000 | 01110000  |  01110000  |
|  6   |     1111110 | 00100000 | 11100000  |  11100000  |
|  7   |    11111110 | 01000000 | 00010111  |  11000001  |
|  8   |   111111110 | 10000000 | 00101110  |  10000011  |
|  9   |  1111111110 | 00000011 | 01011100  |  00010111  |
|  10  | 11111111110 | 00000110 | 10111000  |  00101110  |
|  11  |           - | 00001100 | 01110001  |  01011100  |
|  12  |           - | 00011000 | 11100010  |  10111000  |
|  13  |           - | 00110000 | 00100111  |  01110001  |
|  14  |           - | 01100000 | 01001110  |  11100010  |
|  15  |           - | 11000000 | 10011100  |  11000101  |
|  16  |           - | 00000111 | 00111001  |  10001011  |
|  17  |           - | 00001110 | 01110010  |  00100111  |
|  18  |           - | 00011100 | 11100100  |  01001110  |
|  19  |           - | 00111000 | 01000111  |  10011100  |
|  20  |           - | 01110000 | 10001110  |  00111001  |
|  21  |           - | 11100000 | 00011101  |  01110010  |
|  22  |           - | 00001111 | 00111010  |  11100100  |
|  23  |           - | 00011110 | 01110100  |  11001001  |
|  24  |           - | 00111100 | 11101000  |  10010011  |
|  25  |           - | 01111000 |     -     |  01000111  |
|  26  |           - | 11110000 |     -     |  10001110  |
|  27  |           - | 00011111 |     -     |  00011101  |
|  28  |           - | 00111110 |     -     |  00111010  |
|  29  |           - | 01111100 |     -     |  01110100  |
|  30  |           - | 11111000 |     -     |  11101000  |
|  31  |           - | 00111111 |     -     |  11010001  |
|  32  |           - | 01111110 |     -     |  10100011  |
|  33  |           - | 11111100 |     -     |  10000111  |
|  34  |           - | 01111111 |     -     |     -      |
|  35  |           - | 11111110 |     -     |     -      |
|  36  |           - | 11111111 |     -     |     -      |