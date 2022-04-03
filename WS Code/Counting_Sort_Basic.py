

# %%
print("Hello world")

# %% Function Counting Sort
def sort_counting(new_list):
    '''
    Precondition: new_list have at least 1 item
    '''
    # find the max
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    # print(max_item)
    # initialize count array
    count_array = [0] * (max_item+1)
    # print(count_array)
    # update input array
    for item in new_list:
        count_array[item] = count_array[item] + 1
    # print(count_array)
    # update input array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1
    # new_list will be sorted
    return new_list

# %% Function Counting Sort Stable
def sort_counting_stable(new_list):
    '''
    Precondition: new_list have at least 1 item
    '''
    # find the max
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
    print(max_item)
    # initialize count array
    count_array = [None] * (max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []
    print(count_array)
    # update input array
    for item in new_list:
        count_array[item].append(item)
    print(count_array)
    # print(count_array)
    # update input array
    # TODO do it urself lol
    # new_list will be sorted
    return new_list

# %% Function Counting Sort Alphabet
def sort_counting_alphabet(new_list):
    '''
    Precondition: new_list have at least 1 item
    '''
    # find the max
    max_item = ord(new_list[0])-97
    for item in new_list:
        item = ord(item)-97
        if item > max_item:
            max_item = item
    print(max_item)
    return
    # initialize count array
    count_array = [0] * (max_item+1)
    # print(count_array)
    # update input array
    for item in new_list:
        count_array[item] = count_array[item] + 1
    # print(count_array)
    # update input array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1
    # new_list will be sorted
    return new_list


# %% Driver Counting Sort 
list_a = [6, 3, 1, 7, 2, 8, 1, 7]
# list_a = ["a","b","a","c","x","a"]
print(list_a)
list_a = sort_counting_stable(list_a)
print(list_a)
# check
# for i in range(0, len(list_a)-1):
#     if list_a[i] <= list_a[i+1]:
#         continue
#     else:
#         print("fail!")
# print("pass")

# %% Driver Radix Sort
list_a = [200,151,291,369,421,671]
# TODO ugh ill finish this later


# %%
print(ord("a"))
print(ord("b"))
print(ord("z"))
print(chr(97))
print(chr(99))

# %%
