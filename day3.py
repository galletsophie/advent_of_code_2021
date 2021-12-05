import pandas as pd 
import numpy as np

# txt format easier than csv on this one
with open('day3.txt') as f:
    lines = f.readlines()

bin_list = [b.replace("\n", "") for b in lines]

# this all seems too convoluted, but couldn't find the easy way to do it with numpy
bin_df = pd.DataFrame([list(b) for b in bin_list])
top_binary_list = bin_df.describe(include=['O']).iloc[2,:]
gamma_binary = "".join(list(top_binary_list))
gamma_int = int(gamma_binary, 2)

epsilon_list = ['1' if b == '0' else '0'  for b in top_binary_list]
epsilon_binary = "".join(list(epsilon_list))
epsilon_int = int(epsilon_binary, 2)

#print(gamma_int * epsilon_int)

# --- Part Two ---


test_df = pd.DataFrame([list(b) for b in ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']])

def get_top_binary(df_column):
    # Return most common value, default in case of equal frequency
    vc = df_column.value_counts()
    if vc[0] == vc[1]:
        return '1'
    else: 
        return vc.index[0]

def last_standing(bin_df, column_index=0, oxygen = True):
    # Recursive function to find last row meeting criteria. 
    ## oxygen: starting at col1, keep rows with most common value in col1, move on to col2 with remaining rows and apply same logic
    ## co2: the over way around, keep rows with least common value in col1, etc.  
    if column_index == bin_df.shape[1]:
        return bin_df
    top_binary = get_top_binary(bin_df[column_index])
    if oxygen == False:
        if top_binary == '1': top_binary = '0'
        else: top_binary = '1'
    top_filtered = bin_df[bin_df[column_index]==top_binary] 
    # 1 row left
    if top_filtered.shape[0] ==1:
        bin_res = "".join(top_filtered.iloc[0])
        int_res = int(bin_res,2)
        return int_res
    return last_standing(top_filtered, column_index+1, oxygen)


test_oxygen = last_standing(test_df)
test_co2 = last_standing(test_df, oxygen=False)
print(test_oxygen,test_co2)

oxygen = last_standing(bin_df)
co2 = last_standing(bin_df, oxygen=False)
print(oxygen, co2, oxygen * co2)
