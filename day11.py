from logging.handlers import DatagramHandler
from re import L
import pandas as pd
import numpy as np
import itertools

def prep_data(csv_name):
    data = pd.read_csv(csv_name, header=None)[0]
    n_row = data.shape[0]
    n_col = len(str(data[0]))
    split_numbers = [int(e) for t in data for e in list(str(t))]
    return np.array(split_numbers).reshape(n_row, n_col)
    

def spread_flash(data, flash_count, accounted_flashes=None):
    n_row, n_col = data.shape
    # Spread for first round of numbers that reached 10 
    flash_coords = np.where(data>=10)
    new_flash=[]
    if accounted_flashes is None:
        accounted_flashes = []
    for i in range(len(flash_coords[0])):
        if len(flash_coords[0])==0:
            continue
        x = flash_coords[0][i]
        y = flash_coords[1][i]
        if [x,y] not in accounted_flashes:
            accounted_flashes.append([x,y])
            data[x,y]+=1
            for i, j in itertools.product(range(x-1,x+2), range(y-1,y+2)):
                if (i>=0) and (j>=0) and [i,j]!= [x,y] and (i<n_row) and (j<n_col):
                    data[i,j]+=1 
                    if data[i,j]>=10 and [i,j] not in new_flash and [i,j] not in accounted_flashes:
                        new_flash.append([i,j])
    # If all the flashes have been accounted for in this step            
    if len(new_flash)==0: 
        data = np.where(data>9, 0, data)
        flash_count += len(np.where(data==0)[0])
        return data, flash_count
    # Otherwise, spread for numbers that just reached 10 or more     
    else:
        return spread_flash(data, flash_count, accounted_flashes)    

def is_sim_flashing(data):
    small_ints = np.arange(10)
    for k in small_ints:
        if np.array_equal(data,np.full(data.shape, k)):
            return True
    else: return False        

lil_test = np.array([10, 1,2,10]).reshape(1,4)
test = prep_data('day11_test.csv')    
data = prep_data('day11.csv')


def main(data):
    flash_count = 0 
    for i in range(10000):
        data = data +1 
        data, flash_count = spread_flash(data, flash_count)
        print(f"Step {i+1}, flash count: {flash_count}\n")  
        if is_sim_flashing(data):
            break
    return flash_count

#print(is_sim_flashing(data))
print(main(data))

# --- Part Two ---

