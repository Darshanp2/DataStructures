class Trie:
    def __init__(self):
        self.root = {"*":"*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = "*"

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '*' in curr_node
    
trie = Trie()
words = ['wait', 'waiter', 'shop', 'shopper']
for word in words:
    trie.add_word(word)

print(trie.does_word_exist('wait'))
print(trie.does_word_exist('waite'))
print(trie.does_word_exist('waiter'))
print(trie.does_word_exist('shop'))
