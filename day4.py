import pandas as pd
import numpy as np

# ---- Test
test_order = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
test_boards = {1: np.array([22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5,1, 12, 20, 15, 19]).reshape(5,5),
        2: np.array([3, 15, 0, 2, 22, 9, 18, 13, 17, 5, 19, 8, 7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12, 6]).reshape(5,5),
        3: np.array([14, 21, 17, 24, 4,10, 16, 15, 9, 19,18, 8, 23, 26, 20,22, 11, 13, 6, 5,2, 0, 12, 3, 7 ]).reshape(5,5)
}
test_mask = {1:np.zeros(25, dtype=int).reshape(5,5), 2:np.zeros(25).reshape(5,5),3:np.zeros(25).reshape(5,5)}

# ---- READ AND FORMAT DATA
df = pd.read_csv('day4.csv')

# That works
str_order = list((df).columns)
nb_order = [int(nb) for nb in str_order]


# That works, must exist a simpler way 
data = df.iloc[:, 0]
board_dict = {}
k = 0
for i in range(0, len(data), 5):
    raw_arr_data = data[i:i+5]
    l_of_l = [sublist.split(" ") for sublist in raw_arr_data]
    single_int_l = [int(item) for sublist in l_of_l for item in sublist if item != '']
    arr = np.array(single_int_l).reshape(5,5)
    board_dict[k] = arr
    k+=1

# ---- HELPER & MAIN FN
# Helper function #1
def is_winning(mask):
    # Return True if one or more of the columns or rows is full of 1 for given mask
    sum_rows = mask.sum(axis=0) 
    sum_cols = mask.sum(axis=1)
    if any({np.where(sum_rows >= 5)[0].shape != (0,), np.where(sum_cols >= 5)[0].shape != (0,)}):
        return True
    else: return False 

# Helper function #2
def compute_score(board, mask, nb):
    # Inverse the mask to keep unmarked numbers and zero out the marked ones 
    # Sum elt of result arr, and multiply by nb
    unmarked_numbers = -board * (mask-np.ones(25).reshape(5,5))
    return unmarked_numbers.sum() * nb

# The main function
def get_winning_score(nb_order, board_dict):
    # Instantiate masks, starting with all 0s
    mask_dict = {}
    for k in board_dict.keys():
        mask_dict[k] = np.zeros(25, dtype=int).reshape(5,5)     

    # For each nb, then for each board, change mask value to 1 for correct location if nb in board 
    for nb in nb_order:
        for k in board_dict.keys():
            board = board_dict[k]
            mask = mask_dict[k]
            nb_loc = np.where(board==nb)
            mask[nb_loc] = 1    
            if is_winning(mask):
                return compute_score(board, mask, nb)

# ---- GET SCORE 
#test_score = get_winning_score(test_order, test_boards)
#print(test_score)
score = get_winning_score(nb_order, board_dict)
print(score)


# --- Part Two ---
def get_winning_score(nb_order, board_dict, loose=True):
    ks = list(board_dict.keys())
    removed_ks=[]
    # Instantiate masks, starting with all 0s
    mask_dict = {}
    for k in ks:
        mask_dict[k] = np.zeros(25, dtype=int).reshape(5,5)     

    # For each nb, then for each board, change mask value to 1 for correct location if nb in board 
    for nb in nb_order:
        for k in ks:
            # Had to go this way instead of using list.remove() otherwise it would skip a nb
            if k in removed_ks:
                continue


            board = board_dict[k]
            mask = mask_dict[k]
            nb_loc = np.where(board==nb)
            mask[nb_loc] = 1    
           
            if is_winning(mask) and loose:
                print(f"removing key {k}")
                removed_ks.append(k)
                if len(removed_ks) == len(ks):
                    score = compute_score(board, mask, nb)
                    print(nb, score, board, mask)
                    return score


test_loose_score = get_winning_score(test_order, test_boards)
print(test_loose_score)    

loose_score = get_winning_score(nb_order, board_dict)
print(loose_score)    