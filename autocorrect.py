class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def suggestions(self, word, max_distance=1):
        suggestions = []
        # Implement Damerau-Levenshtein algorithm to find suggestions
        # based on the max_distance parameter
        # Populate 'suggestions' list with words closest to 'word'
        return suggestions

# Assuming 'dictionary.txt' contains a list of words, one per line
def load_dictionary():
    trie = Trie()
    with open('dictionary.txt', 'r') as file:
        words = file.readlines()
        for word in words:
            trie.insert(word.strip())
    return trie

def main():
    dictionary_trie = load_dictionary()
    while True:
        user_input = input("Enter a word: ")
        if user_input == 'exit':
            break
        if user_input.isalpha():
            if dictionary_trie.search(user_input):
                print(f"'{user_input}' is a valid word.")
            else:
                suggestions = dictionary_trie.suggestions(user_input)
                print(f"Did you mean {suggestions}?")
        else:
            print("Please enter alphabetic characters only.")

if __name__ == "__main__":
    main()
