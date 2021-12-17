from os import EX_SOFTWARE
import pandas as pd
import numpy as np

test_list = [16,1,2,0,4,2,7,1,2,14]
actual_list = list(pd.read_csv("day7.csv", header=None).iloc[0])

def get_min_fuel(l):
    # Future: Keep only close to median
    fuel = dict()
    min_fuel = max(l) * len(l)
    for i in range(max(l)): 
        fuel[i] = sum([abs(e - i) for e in l])
        if fuel[i]<= min_fuel:
            min_fuel = fuel[i]
    return min_fuel

test_min = get_min_fuel(test_list)
actual_min = get_min_fuel(actual_list)
print(actual_min)

# --- Part Two ---
def get_min_fuel(l):
    # Future: Keep only close to median
    fuel = dict()
    min_fuel = max(l)**3 * len(l) #something big
    for i in range(max(l)): 
        fuel[i] = sum([abs(e - i) * (abs(e - i)+1) / 2  for e in l])  
        if fuel[i]<= min_fuel:
            min_fuel = fuel[i]
    return min_fuel

test_min = get_min_fuel(test_list)
print(test_min)
actual_min = get_min_fuel(actual_list)
print(actual_min)