""" FIT2004 Assignment 2

__author__ = "Er Tian Ru"

References:
Coin Change 2 video https://youtu.be/ruMqWViJ2_U
Code from Coin Change 2 video https://gist.github.com/SuryaPratapK/90c533cacb70ad71ac75810889748818
geeksforgeeks coin change https://www.geeksforgeeks.org/coin-change-dp-7/
Week 4 Lecture recording Dynamic Programming https://youtu.be/s7gpf0Q1i_8
geeksforgeeks unbounded knapsack https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
"""

# %%


def count_encounters(target_difficulty: int, monster_list: list) -> int:
    """ 
    Returns the number of different sets of monsters whose difficulties sum to target difficulty where
    each type of monster may be used more than once.

    :param target_difficulty: a non-negative integer repersenting the target difficulty
    :param monster_list: a list of tuples each representing a type of monster. [("bear", 5), ("imp", 2)]
                         The first value of each tuple is a string name of the monster type.
                         The second value is a positive integer representing the difficulty of the monster type.

    :raises: an Exception if target_difficulty < 0

    :returns: an integer number of different sets of monsters whose difficulties sum to target_difficulty

    :complexity: O(DM) where
                    D is the value of target_difficulty
                    M is the length of monster_list
    """
    if target_difficulty < 0:
        raise Exception('target_difficulty cannot negative')

    # initialize 2D memo (rows = monster dificulties, columns = target dificulties)
    memo = [[0 for _ in range(target_difficulty + 1)]
            for _ in range(len(monster_list) + 1)]

    # fill up first column with 1s (only 1 way to get target difficulty 0)
    for row in range(len(monster_list) + 1):
        memo[row][0] = 1

    # fill in rest of memo
    for row in range(1, len(monster_list) + 1):
        for col in range(1, target_difficulty + 1):
            # if able to include monster difficulty w/in current difficulty
            if col >= monster_list[row - 1][1]:
                # include monster difficulty
                memo[row][col] = memo[row][col -
                                           monster_list[row - 1][1]] + memo[row - 1][col]
            else:
                # exclude monster difficulty
                memo[row][col] = memo[row - 1][col]

    return memo[len(monster_list)][target_difficulty]


# %%
def best_lamp_allocation(num_p: int, num_l: int, probs: list) -> float:
    """
    Returns the highest probability of all plants that can be obtained by allocating lamps to plants optimally.

    :param num_p: a positive integer representing the number of plants
    :param num_l: a positive integer representing the number of lamps available
    :param probs: a list of lists containing floats from 0 to 1 inclusive, 
                  where probs[i][j] represents the probability that plant i will be ready in time if given j lamps

    :returns: the highest probability of all plants that can be obtained by allocating lamps to plants optimally

    :time complexity: O(PL2), where P is num_p, and L is num_l
    :space complexity: O(PL), where P is num_p, and L is num_l    
    """
    # return 0 if empty probs
    if not probs:
        return 0

    # initialize 2D memo (rows = plants, columns = number of lamps)
    memo = [[0 for _ in range(num_l + 1)] for _ in range(num_p + 1)]

    # plant 0, base case of 1
    for lamp in range(num_l + 1):
        memo[0][lamp] = 1

    # fill in rest of memo
    for plant in range(1, num_p + 1): # loop through each plant
        for lamp_memo in range(num_l + 1): # loop through each number of lamps for memo
            for lamp_probs in range(len(probs[0])): # loop through each number of lamps for probability
                    if num_p <= len(probs) and lamp_probs <= lamp_memo:
                        memo[plant][lamp_memo] = max(
                            memo[plant][lamp_memo], memo[plant - 1][lamp_memo - lamp_probs] * probs[plant-1][lamp_probs])

    return memo[num_p][num_l]


# %%
if __name__ == '__main__':
    pass

# %%
