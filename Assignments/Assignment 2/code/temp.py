# %%
def best_lamp_allocation(num_p: int, num_l: int, probs: list) -> float:
    memo = [[0 for _ in range(num_l + 2)] for _ in range(num_p)]

    # fill up first column with 1s (base case = 1)
    for i in range(num_p):
        memo[i][0] = 1
 
    for i in range(num_p):
            for j in range(1, num_l + 2):
                for k in range(num_l + 1): # go through probablity 
                    if i > 0:
                        memo[i][j] = memo[i-1][j]
                    if k <= j-1:
                        prob = probs[i][k] * memo[i][j-k-1]
                        if prob > memo[i][j]:
                            memo[i][j] = prob