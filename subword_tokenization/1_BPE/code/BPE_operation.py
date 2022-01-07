# !usr/bin/env python3
# coding=utf-8

# Algorithm 1 Learn BPE operations

import re, collections
from pprint import pprint


def get_status(vocab):

    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair,v_in):
    v_out = {}
    bigram = re.escape(" ".join(pair))
    p = re.compile(r'(?<!\S)'+bigram+r'(?!\S)')
    for word in v_in:
        w_out = p.sub("".join(pair),word)
        v_out[w_out] = v_in[word]
    return v_out


if __name__ == "__main__":
    

    vocab = {
        "l o w </w>":5,
        "l o w e r </w>":2,
        "l o w e s t </w>":2,
        "n e w e s t </w>":6,
        "w i d e s t </w>":3,
    }

    num_merges = 10

    pprint(vocab)

    for i in range(num_merges):
        pairs = get_status(vocab=vocab)

        print("#"*15,"iteration-{}".format(i),"#"*15)

        print("Available pairs:") 
        for pair,count in pairs.items():
            print(pair,count)

        best = max(pairs, key=pairs.get)
        print("Best pair in this iteration:", best, pairs.get(best))
        
        vocab = merge_vocab(best,vocab)
        print("Updated vocab:",vocab)
    
    final_vocab = []
    for word,count in vocab.items():
        final_vocab.extend(word.split())
    final_vocab = sorted(list(set(final_vocab)),key=len)
    print("Final vocab:",final_vocab)