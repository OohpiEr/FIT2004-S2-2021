# %%
class Node:
    def __init__(self, data=None, level=None, size=27) -> None:
        # terminal at index 0
        self.link = [None] * size
        # data payload
        # self.name = None
        # self.age = None
        # self.address = None
        self.data = data
        # level of node
        self.level = level


# %%
class Trie:
    def __init__(self) -> None:
        self.root = Node(level=0)

    # iterative insert
    def insert(self, key, data=None) -> None:
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

        # go through terminal, index = 0
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        else:
            # if path doesn't exist
            # create a new node
            current.link[index] = Node(level=count_level)
            current = current.link[index]

        # add in the payload
        current.data = data

    # recursive insert -> INCOMPLETE
    def insert_recursion(self, key, data=None):
        current = self.root
        self.insert_recursion_aux(current, key, data)

    def insert_recursion_aux(self, current, key, data=None):
        if len(key) == 0:
            # base case
            return
        else:
            # calculate index
            # $ = 0, a = 1, b = 2, ...
            index = ord(key[0]) - 97 + 1

            if current.link[index] is not None:
                # if path exists
                current = current.link[index]
            else:
                # if path doesn't exist
                # create a new node
                current.link[index] = Node()
                current = current.link[index]

            # recursion step
            # KEY[1:] IS BAD MINUS MARKS -> SLICE NOT ALLOWED!!
            self.insert_recursion_aux(current, key[1:], data)
            # hint: use key[i] & check if i == ? in base step (what?)

    def search(self, key) -> None:
        # begin from root
        current = self.root

        # go through key 1 by 1
        for char in key:
            print(current.level)

            # calculate index
            # $ = 0, a = 1, b = 2, ...
            index = ord(char) - 97 + 1

            if current.link[index] is not None:
                # if path exists
                current = current.link[index]
            else:
                # if path doesn't exist
                raise Exception(str(key) + " doesn't exist")

        # go through terminal, index = 0
        index = 0
        print(current.level)
        if current.link[index] is not None:
            current = current.link[index]
        else:
            # if path doesn't exist
            raise Exception(str(key) + " doesn't exist")

        print(current.level)
        return current.data
        # add in the payload
        current.data = data

# %%


def test():
    test = Trie()

    # test insert
    test.insert("lol", ["hello", "it's me"])
    test.insert("loa", "456")
    test.insert("lob", "789")
    test.insert("uwu", None)

    # test search
    try:
        print(test.search("lol"))
    except Exception as e:
        print(e)

    try:
        print(test.search("loa"))
    except Exception as e:
        print(e)

    try:
        print(test.search("los"))
    except Exception as e:
        print(e)

    try:
        print(test.search("lo"))
    except Exception as e:
        print(e)

    try:
        print(test.search("uwu"))
    except Exception as e:
        print(e)


# %%
if __name__ == '__main__':
    test()

# %%
