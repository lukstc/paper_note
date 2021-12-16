# {a, ##b, ##c, ##cdy, ##dz, abcdx}
from pprint import pprint,pformat

class Trie:
    def __init__(self) -> None:
        self.trie = {}

    def insert(self, token:str) -> None:
        curr = self.trie
        for w in token:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        # curr['#'] = 1

    def search(self, word):
        curr = self.trie
        for w in word:
            print(curr)
            print(w)
            if w not in curr:
                print("Search: not in trie")
                return False
            curr = curr[w]
        print("Search: in trie")
        return True

    def starts_with(self,prefix):
        curr = self.trie
        for w in prefix:
            if w not in curr:
                print("Prefix: not in trie")
                return False
            curr = curr[w]
        print("Prefix: in trie")
        return True

if __name__ == "__main__":
    
    my_trie = Trie()

    vocabulary = {"a", '##b', '##c', '##cdy', '##dz', "abcdx"}
    
    for item in vocabulary:
        # print(item)
        my_trie.insert(item)
    
    pprint(my_trie.trie, width=1)

    my_trie.search("abcdx")

    # my_trie.starts_with("abdc")
    

