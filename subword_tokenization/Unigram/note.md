# Unigram

Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates

BPE的解决了准备Vocab的问题，利用greedy算法，也解决了分词sub-word segmentation的问题。但是BPE的sub-word segmentation使用的是greedy拆分的方法，但在实际当中，一个词对应vocab可能有用不同的subwords对应的多种拆词的选项。



Kudo在论文中介绍了一种新的方法来解决上述问题：利用概率论的方法选取最合适的拆分方案

Denote $X$ as a subword sequence of length $n$

一个subword sequence（本质上是一个词或者句子）可以表示为：$X=(x_1, x_2, x_3 ... x_n)$

$P(x_i)$：表示独立的subword $X_i$分布。

那么对应的$X$出现概率可以表示为以下公式
$$
P(X) = \prod_{i=1}^n P(x_i)
$$

with 
$$
\sum_{x \in V}P(x) = 1,
$$

【$V$ : Vocabulary 全集】

可能性最高的分词sequence组合是通过应用

- [Expectation-Maximization最大期望算法](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
- [Viterbi Algorithm维特比算法](https://en.wikipedia.org/wiki/Viterbi_algorithm)

The vocabulary set $V$ is indeed undertermined at the very beginning and cannot be solved simultaneously with the maximization task. A workaround is to provide a seed vocabulary as the initial (reasonably big enough) vocabulary, and shrink the seed vocabulary during training until a desired vocabulary size is reached.

初始阶段Vocab无法确定，解决方案是先准备一个足够大的vocab，然后慢慢在训练过程中缩小至理想的size；





## Reference

- https://www.yanxishe.com/columnDetail/26326
- https://zhuanlan.zhihu.com/p/86965595
- https://mp.weixin.qq.com/s?__biz=MzI4MDYzNzg4Mw==&mid=2247520012&idx=3&sn=e92b8d44b747150c7807a37d3b11f70b&chksm=ebb7b7d8dcc03ece601d87476bd43457d4461d649aef8cdfbc61fe955814f243fafcc1cdf80f#rd
- https://everdark.github.io/k9/notebooks/ml/natural_language_understanding/subword_units/subword_units.nb.html#121_expectation-maximization