"""
Assignment 2 Task 1 - Lexical position

References:
FIT2004 Lecture 06 Trie - https://youtu.be/gr647pytPso
"""

__author__ = "Er Tian Ru"


# %%
class Node:
    """
    Node class for Trie
    """
    def __init__(self, level=None, size=27) -> None:
        # terminal at index 0
        self.link = [None] * size
        self.level = level  # level of node
        self.payload = 0  # payload

# %%
class Trie:
    """
    Trie class
    """

    def __init__(self) -> None:
        self.root = Node(level=0)

    def insert(self, key) -> None:
        """ iterative insert function. Inserts a key into the Trie.

        :param key: the string to be inserted into the Trie

        :complexity: O(k) where k is the number of characters in key
        """
        count_level = 1

        # begin from root
        current = self.root

        # go through key 1 by 1
        for char in key:
            # calculate index
            # $ = 0, a = 1, b = 2, ...
            index = ord(char) - 97 + 1

            if current.link[index] is not None:
                # if path exists
                current = current.link[index]
            else:
                # if path doesn't exist
                # create a new node
                current.link[index] = Node(level=count_level)
                current = current.link[index]

            count_level += 1
            current.payload += 1  # add in the payload

        # go through terminal, index = 0
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        else:
            # if path doesn't exist
            # create a new node
            current.link[index] = Node(level=count_level)
            current = current.link[index]

        current.payload += 1  # add in the payload

    def search(self, key: str) -> int:
        """ Search through the Trie and returns the number of words with a higher lexicographicall order.

        :param key: the string to be inserted into the Trie

        :return: an integer number of words with a higher lexicographicall order.

        :complexity: O(k) where k is the number of characters in key
        """
        # begin from root
        current = self.root
        index = 0
        num_words_lex = 0

        # go through key 1 by 1
        for i in range(len(key)):
            # calculate index
            # $ = 0, a = 1, b = 2, ...
            index = ord(key[i]) - 97 + 1
            if current.link[index] is not None:
                # if path exists
                # O(1)
                for j in range(len(current.link)):
                    if current.link[j] is not None and j > index:
                        num_words_lex += current.link[j].payload
                current = current.link[index]
            else:
                # if path doesn't exist
                raise Exception(str(key) + " doesn't exist")

        # O(1)
        # add child nodes
        for i in range(1, len(current.link)):
            if current.link[i] is not None:
                num_words_lex += current.link[i].payload

        return num_words_lex


def lex_pos(text: list, queries: list) -> list:
    """
    :param text: an unsorted list of strings consisting of only lowercase a-z characters
    :param queries: a list of strings consisting only of lowercase a-z characters with each string
                    being a prefix of some string in text.

    :return: a list of numbers where the ith number is the number of words in text which 
             are lexicographically greater than the ith element of queries

    :complexity: O(T + Q) time, where
                    T is the sum of the number of characters in all strings in text
                    Q is the total number of characters in queries
    """
    trie = Trie()
    lex_pos_list = []

    # O(T)
    for query in text:
        trie.insert(query)

    # O(Q)
    for query in queries:
        lex_pos_list.append(trie.search(query))

    return lex_pos_list


# %%
if __name__ == "__main__":
    text = ["aaa", "bab", "aba", "baa", "baa", "aab", "bab"]
    queries = ["", "a", "b", "aab"]
    print(lex_pos(text, queries))
    # # output [7, 7, 4, 5]

# %%
