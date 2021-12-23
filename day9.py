import pandas as pd
import numpy as np

data= pd.read_csv("day9.csv", header=None)
test = """2199943210
3987894921
9856789892
8767896789
9899965678"""

test_arr = np.array([list(map(int,list(n))) for n in test.split("\n")])
data_arr = np.array([list(map(int,list(row))) for row in data[0]])

def get_surrounding(arr, i, j, n_rows, n_cols):
    # This is gross 
    # top row
    if i == 0:
        if j == 0: #top left corner
            return [arr[i, j+1], arr[i+1, j]]
        elif j==n_cols-1:
            return [arr[i, j-1], arr[i+1, j]]
        else:    
            return [arr[i, j-1], arr[i, j+1], arr[i+1, j]]
    # bottom row        
    elif i==n_rows-1:
        if j == 0:
            return [arr[i, j+1], arr[i-1, j]]
        elif j==n_cols-1:
            return [arr[i, j-1], arr[i-1, j]]
        else:    
            return [arr[i, j-1], arr[i, j+1], arr[i-1, j]]
    # leftmost col, center rows
    elif j==0:
        return [arr[i+1, j], arr[i-1, j], arr[i, j+1]]  
    # rightmost col, center rows  
    elif j==n_cols-1:
        return [arr[i+1, j], arr[i-1, j], arr[i, j-1]]

    # center rows and cols
    else:
        return [arr[i+1, j], arr[i-1, j], arr[i, j+1], arr[i, j-1]]          


def get_local_minima(arr):
    local_mins = []
    n_rows, n_cols = arr.shape
    for i,row in enumerate(arr):
        for j,val in enumerate(row):
            surroundings = get_surrounding(arr, i, j, n_rows, n_cols)
            if val < min(surroundings):
                local_mins.append(val)
    return sum(local_mins) + len(local_mins)
    #return local_mins, sum(local_mins) + len(local_mins)

#print(get_local_minima(test_arr))
print(get_local_minima(data_arr))

# --- Part Two ---
