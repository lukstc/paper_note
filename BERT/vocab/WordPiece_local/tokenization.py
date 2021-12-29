# coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import re
import unicodedata
import six
# import tensorflow as tf

from tokenization_tool import load_vocab, BasicTokenizer, WordpieceTokenizer, convert_tokens_to_ids


class FullTokenizer(object): 
	def __init__(self, vocab_file, do_lower_case=True):
		self.vocab = load_vocab(vocab_file)
		self.basic_tokenizer = BasicTokenizer(do_lower_case=do_lower_case)
		self.wordpiece_tokenizer = WordpieceTokenizer(vocab=self.vocab)

	def tokenize(self, text):
		split_tokens = []
		for token in self.basic_tokenizer.tokenize(text):
			for sub_token in self.wordpiece_tokenizer.tokenize(token):
				split_tokens.append(sub_token)
		
		return split_tokens

	def convert_tokens_to_ids(self, tokens):
		return convert_tokens_to_ids(self.vocab, tokens)


if __name__ == "__main__":
	
	vocab_file = "bert-large-uncased-vocab.txt"
	
	full_tokenizer = FullTokenizer(vocab_file=vocab_file, do_lower_case=True)
    
	temp = full_tokenizer.tokenize(
		"""
		Hello world, 
		bert-large-uncased-vocab, 
		supercalifragilisticexpialidocious, 
		é and e\u0301
		"""
	)
	print(temp)

	temp = full_tokenizer.convert_tokens_to_ids(temp)
	print(temp)