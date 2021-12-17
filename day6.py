import pandas as pd
import numpy as np

test_initial_state = [3,4,3,1,2]
initial_state = list(pd.read_csv("day6.csv",header=None).iloc[0])

def next_state(state,iter_count, max_iter):
    print(iter_count)    
    new_state = [fish-1 if fish!=0 else 6 for fish in state] + [8] * len([1 for fish in state if fish==0])
    iter_count+=1
    if iter_count==max_iter:
        #print(new_state)
        return new_state
    return next_state(new_state, iter_count, max_iter)




#test_18d = next_state(test_initial_state, 0, 18)
#print(len(test_18d))

#actual_80 = next_state(initial_state, 0,80)
#print(len(actual_80))

#--- Part Two ---
## Option1: run fn for 1 initial timer at a time to get nb of fish at 256, then multiply by count for given nb. 
## Option2: save the results better / break down the command, and reuse past computation.
## Option3: find the maths formula
test_0_256d = next_state([0],0,256)