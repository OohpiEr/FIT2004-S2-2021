""" FIT2004 Assignment 1

__author__ = "Er Tian Ru"

References:
Week 2 Lecture recording counting sort https://youtu.be/Ww0kYGWij58?t=829
Week 2 Lecture recording radix sort https://youtu.be/Zw5IxI_ccGY
Week 4 tutorial recording https://youtu.be/KYXPA_9gkjA
geeksforgeeks radix sort https://www.geeksforgeeks.org/radix-sort/
"""
from hashlib import new
import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np

# %%
def num_rad_sort(nums: list, b: int) -> list:
    """ 
    Performs a radix sort on a list given a number base (e.g. base 10, base 2).

    :param nums: a list of integers
    :param b: an integer, with value >= 2  

    :returns: a list of integers sorted into ascending numerical order

    :raises: an Exception when preconditions are violated

    :precondition 1: new_list have at least 1 item 
    :precondition 2: b >= 2

    :complexity: O((n+b)*log(b)M) where 
                    n is the length of nums
                    b is the value of b
                    M is the numerical value of the maximum element of nums
    """
    if not nums:
        raise Exception('Nums cannot be empty')
    elif b < 2:
        raise Exception('b cannot be less than 2')

    # find the max and copy nums into new_list
    max_item = nums[0]
    new_list = []
    for item in nums:
        new_list.append(item)
        if item > max_item:
            max_item = item

    # get maximum column
    if max_item > 0:
        max_col = math.floor(math.log(max_item, b) + 1)
    else:
        max_col = 1

    # Do counting sort for every digit in each column
    col = 0
    while max_col > col:
        counting_sort(new_list, b, col)
        col += 1

    return new_list

# %%
def interest_groups(data: list) -> list:
    """
    :param list: a list of 2-element tuples. 
                    The first element in the tuple is a unique nonempty string of lowercase a-z with no spaces or punctuation. 
                    The second element is a nonempty list of nonempty strings of lowercase a-z and also spaces

    :return: a list of lists grouped by the 2nd element in the input tuple, sorted by ascending
             alphabetical order.

    :complexity: O(NM), where N is the number of elements in data and
                              M is the maximum number of characters among all sets of the 2nd element in the tuple
    """
    if not data:
        raise Exception('Data cannot be empty')

    # O(n)
    new_list = []
    for item in data:
        new_list.append(item)

    # O(nm)
    # sort interest in order
    for tup in new_list:
        radix_sort_str(tup[1])

    # O(nm)
    # sort tuples according to interests
    radix_sort_interest(new_list)

    # O(n)
    # group similar interests into list
    output_list = [[new_list[0][0]]]
    j = 0
    for i in range(len(new_list)-1):
        if new_list[i][1] == new_list[i+1][1]:
            output_list[j].append(new_list[i+1][0])
        else:
            output_list.append([new_list[i+1][0]])
            j += 1

    # O(n)
    # sort names
    for name_list in output_list:
        radix_sort_str(name_list)

    return output_list

# %%
def data_generator_plot() -> None:
    """
    Genarates data for task2 and plots a graph.
    """
    # generate data
    random.seed("FIT2004S22021")
    data1 = [random.randint(0, 2**25) for _ in range(2**15)]
    data2 = [random.randint(0, 2**25) for _ in range(2**16)]
    bases1 = [2**i for i in range(1, 23)]
    bases2 = [2*10**6 + (5*10**5)*i for i in range(1, 10)]

    # run base_timer
    y1 = base_timer(data1, bases1)
    y2 = base_timer(data2, bases1)
    y3 = base_timer(data1, bases2)
    y4 = base_timer(data2, bases2)

    # plot
    fig, (ax1, ax2) = plt.subplots(1, 2)  # Create a figure and an axes.

    ax1.plot(bases1, y1, label='y1')
    ax1.plot(bases1, y2, label='y2')
    ax1.set_xscale('log')
    ax1.set_xlabel('bases1')  # Add an x-label to the axes.
    ax1.set_ylabel('time')  # Add a y-label to the axes.
    ax1.set_title("Graph 1")  # Add a title to the axes.
    ax1.legend()  # Add a legend.

    ax2.plot(bases2, y3, label='y3')  # ... and some more.
    ax2.plot(bases2, y4, label='y4')    # ... and some more.
    ax2.set_xlabel('bases2')  # Add an x-label to the axes.
    ax2.set_ylabel('time')  # Add a y-label to the axes.
    ax2.set_title("Graph 2")  # Add a title to the axes.
    ax2.legend()  # Add a legend.

    plt.show()

# %% Function Counting Sort Stable
def counting_sort(new_list: list, b: int, col: int) -> list:
    '''
    Implementation of counting_sort for num_rad_sort.

    :param new_list: a list of integers
    :param col: an integer representing the column (place) of the number
    :param b:an integer with value >= 2, represents the number base 

    :returns: a list of integers sorted into ascending numerical order based on the column (place)

    Precondition: new_list have at least 1 item
    :complexity: O(n + b), where 
                    n is the length of the input list 
                    b is the base given in the input.
    '''

    # initialize count array
    count_array = [None] * (b + 1)
    for i in range(len(count_array)):
        count_array[i] = []  # initialize separate lists

    # update count array
    for item in new_list:
        digit = (item//(b**col)) % b
        count_array[digit].append(item)

    # update input array
    i = 0
    for bucket in count_array:
        if bucket:
            for item in bucket:
                new_list[i] = item
                i += 1

    # return sorted new_list
    return new_list

# %%
def base_timer(num_list: list, base_list: list) -> list:
    """
    A fuction that calculates the time taken to run num_rad_sort() given a list of data and a list of bases.

    :param num_list: a list of integers (data)
    :param base_list: a list of integers (base), all with values >= 2, sorted ascending

    :return: a list of numbers where element i in this list is the time taken to run num_rad_sort() using element i from base_list as the base.
    """
    base_timer = []

    for base in base_list:
        start_time = time.time()
        num_rad_sort(num_list, base)
        base_timer.append(time.time() - start_time)

    return base_timer

# %%
def map_char(count_array: list, item, col: int) -> None:
    """
    Maps item to the count_array 

    :param count_array: the count_array
    :param item: the item to be mapped
    :param col: the column to access the character

    :complexity: O(1)
    """
    if col < len(item):
        # char exists
        char_ascii = ord(item[col])
        if char_ascii == 32:
            # space
            count_array[1].append(item)
        else:
            # a - z
            count_array[char_ascii - 95].append(item)
    else:
        # char does not exist
        count_array[0].append(item)

# %%
def counting_sort_str(new_list: list, col: int) -> list:
    """
    Performs a counting sort on a list of strings based on column

    :param new_list: a list of strings
    :param col: current column to sort by

    :returns: a list of strings sorted into ascending alphabetical order by the column

    :complexity: O(n), where n is the number of elements in new_list
    """
    # O(28)
    # initialize count array
    count_array = [None] * (28)
    for i in range(len(count_array)):
        count_array[i] = []  # initialize separate lists

    # O(n)
    # update count array
    for item in new_list:
        map_char(count_array, item, col)

    # O(n)
    # update input array
    i = 0
    for bucket in count_array:
        if bucket:
            for item in bucket:
                new_list[i] = item
                i += 1

    # return sorted new_list
    return new_list

# %%
def radix_sort_str(new_list: list) -> list:
    """ 
    Performs a radix sort on a list of strings

    :param new_list: a list of strings

    :returns: a list of strings sorted into ascending alphabetical order

    :complexity: O(nm), where n is the number of elements in new_list and
                              m is the length of the longest word in new_list  
    """

    # return list if it's empty
    if not new_list:
        return new_list

    # O(n)
    # find max word length
    max_len = len(new_list[0])
    for item in new_list:
        if len(item) > max_len:
            max_len = len(item)

    # O(nm)
    # sort in order from longest to shortest
    col = max_len - 1
    while col >= 0:
        counting_sort_str(new_list, col)
        col -= 1

    return new_list

# %%
def map_char_interest(count_array: list, tup: tuple, col: int) -> None:
    """
    Maps tup to the count_array 

    :param count_array: the count_array
    :param tup: the tup to be mapped
    :param col: the column to access the character

    :complexity: O(1)
    """
    concatenated_interests = "".join(tup[1])
    if col < len(concatenated_interests):
        # char exists
        char_ascii = ord(concatenated_interests[col])
        if char_ascii == 32:
            # space
            count_array[1].append(tup)
        else:
            # a - z
            count_array[char_ascii - 95].append(tup)
    else:
        # char does not exist
        count_array[0].append(tup)

# %%
def counting_sort_interest(new_list: list, col: int) -> list:
    """
    Performs a counting sort on a list of tuples where the second element is a list of string

    :param new_list: a list of tuples where the second element is a list of string
    :param col: current column to sort by

    :returns: a list of tuples sorted by the second element

    :complexity: O(n), where n is the number of elements in new_list
    """
    # O(28)
    # initialize count array
    count_array = [None] * (28)
    for i in range(len(count_array)):
        count_array[i] = []  # initialize separate lists

    # O(n)
    # update count array
    for tup in new_list:
        map_char_interest(count_array, tup, col)

    # O(n)
    # update input array
    i = 0
    for bucket in count_array:
        if bucket:
            for item in bucket:
                new_list[i] = item
                i += 1

    # return sorted new_list
    return new_list

# %%
def radix_sort_interest(new_list: list) -> list:
    """
    Performs a radix sort on a list of tuples where the second element is a list of string

    :param new_list: a list of tuples where the second element is a list of string

    :returns: a list of tuples sorted by the second element

    :complexity: O(nm), where n is the number of elements in new_list and
                              m is the length of the longest word in new_list  
    """

    # O(nm)
    # find maximum number of characters among all sets of liked things
    max_len = 0
    for tup in new_list:
        if len("".join(tup[1])) > max_len:
            max_len = len("".join(tup[1]))

    # O(nm)
    # sort in alphabetical order
    col = max_len - 1
    while col >= 0:
        counting_sort_interest(new_list, col)
        col -= 1

    return new_list

# %%
if __name__ == '__main__':
    data_generator_plot()

# %%
