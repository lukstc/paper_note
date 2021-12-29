# vocab prepare

Summary: 最主要的区别在于对于whitespace的处理，各自具体prepare vocab的方法有多种（例如BPE）并不是本质上的区别

main topic(s):
- compare wordPiece & sentencePiece
- learn how do they prepare vocab/dict

tokenizing text: 将text文本转化为words，subwords,然后根据mapping、lookup table转化为ID的过程

- [1] space, punctuation, rule-based
- [2] Subword tokenization
  - Byte-Pair Encoding (BPE)
  - WordPiece
  - Unigram
  - SentencePiece

## Space, Punctuation, Rule-based

直观，简单，但是分出来的词典很大

## Subword tokenization

- Subword tokenization是word-level 和 character-level tokenization的混合体。
- Subword tokenization算法基于以下原则
  - 不应将常用词分解为较小的子词，而应将稀有词分解为有意义的子词，
  - 即frequently used words should not be split into smaller subwords, but rare words should be decomposed into meaningful subwords.

### Byte-Pair Encoding (BPE)

过程

- pre-tokenization: 创建unique单词list，并在统计频率
  - `[("hug",10), ("pug",5),("pun",12) ,("bun",4) ,("hugs",5)]`
- create base vocabulary: `['b', 'g', 'h', 'n', 'p', 's', 'u', ]`
  - split based on base-vocabular: `[("h,u,g",10), ("p,u,g",5),("p,u,n",12) ,("b,u,n",4) ,("h,u,g,s",5)]`
  - 计算频率并合并
![BPE](document.asset/BPE.png)
- 停止合并（训练）；合并后的词典vocabulary可以应用于新的单词（前提是没有新增的，未曾见到过的标点符号）

### WordPiece

用于BERT的subword分词器
具体准备过程与参考[Google - Tensorflow](https://www.tensorflow.org/text)

### SentencePiece

[Google SentencePiece Model](https://github.com/google/sentencepiece#train-sentencepiece-model)
区别与WordPiece地方在于

- 是否需要预分词：WordPiece 需要先（通过空格，逗号等）分成words list再进行分词到subword level，sentencePiece可以直接使用sentences作为input
  - google `text.BertTokenizer` 和 `text.WordPieceTokenizer` 都使用了WordPiece的逻辑，
  - 但`text.BertTokenizer`为`text.WordPieceTokenizer`的higher level的interface，可以直接take sentences as input
  - `text.WordPieceTokenizer`只能take words as input

- 适用语言：
  - WordPiece适用于英语等通过标识分割的文本，但并不适合中文日文等基于语义的文本
  - SentencePiece也可适用于英语和中文类文本
  - "This tutorial builds a Wordpiece vocabulary in a top down manner, starting from existing words. This process doesn't work for Japanese, Chinese, or Korean since these languages don't have clear multi-character units. To tokenize these languages conside using `text.SentencepieceTokenizer`, `text.UnicodeCharTokenizer` or [this approach](https://tfhub.dev/google/zh_segmentation/1)."

## Reference
- [1] [CSDN - kaiyin_hzau - BPE, WordPiece, SentencePiece](https://blog.csdn.net/qq_27586341/article/details/113424560)
- [2] [CSDN - 满腹的小不甘 - tokenizers in Transformers：BPE、WordPiece，SentencePiece](https://blog.csdn.net/qq_27586341/article/details/113424560)
- [3] [towardsdatascience - Jonathan Kernes - SentencePiece Tokenizer Demystified](https://towardsdatascience.com/sentencepiece-tokenizer-demystified-d0a3aac19b15)