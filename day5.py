import pandas as pd
import numpy as np

def ingest_data(csv_file):
    raw = pd.read_csv(csv_file, header=None)
    split_cols = raw[1].str.split(" ->", expand=True)
    data = pd.DataFrame({'x1': raw[0], 'y1': split_cols[0].astype(int), 'x2': split_cols[1].astype(int), 'y2':raw[2]})
    return data

def get_frame_corners(data):
    top_left = (min(data.x1.min(), data.x2.min()) , min(data.y1.min(), data.y2.min()))
    bottom_right = (max(data.x1.max(), data.x2.max()) , max(data.y1.max(), data.y2.max()))

    return top_left, bottom_right

def get_count_two_lines(data,br):
    canvass = np.zeros((br[0]+1)*(br[1]+1)).reshape(br[0]+1, br[1]+1)
    for row in data.iterrows():
        x1, y1, x2, y2 = row[1]
        #print(f"({x1}, {y1}) ->  ({x2}, {y2})")
        if x1 == x2:
            ya = min(y1, y2)
            yb = max(y1, y2)
            canvass[x1, ya:yb+1] +=1 
        elif y1 == y2:
            xa = min(x1, x2)
            xb = max(x1, x2)
            canvass[xa:xb+1, y1]+=1 
        #print(canvass).transpose()       
    return len(np.where(canvass >= 2)[0])    

test_data = ingest_data("day5_test.csv")
data = ingest_data("day5.csv")

test_tl, test_br = get_frame_corners(test_data)
tl, br =get_frame_corners(data)


print(get_count_two_lines(test_data,test_br))
print(get_count_two_lines(data, br))


# --- Part Two ---
def get_count_two_lines(data,br):
    # New version
    canvass = np.zeros((br[0]+1)*(br[1]+1)).reshape(br[0]+1, br[1]+1)
    for row in data.iterrows():
        x1, y1, x2, y2 = row[1]
        xa = min(x1, x2)
        xb = max(x1, x2) 
        ya = min(y1, y2)    
        yb = max(y1, y2)
        if x1 == x2: 
            print(f"VERTICAL: [{xa}, {ya}:{yb+1}]")
            canvass[x1, ya:yb+1] +=1 
        elif y1 == y2:
            print(f"HORIZONTAL: [{xa}:{xb+1}, {ya}]")
            canvass[xa:xb+1, y1]+=1 
        elif (x1-x2)/(y1-y2)==1: #DIAG
            print(f"DIAG: ({xa},{ya}) -> ({xb},{yb})")
            for i in range(abs(xa-xb)+1):
                canvass[xa+i, ya+i]+=1
        elif (x1-x2)/(y1-y2)==-1:
            print(f"COUNTER DIAG: ({xa},{yb}) -> ({xb},{ya})") 
            for i in range(abs(xa-xb)+1):
                canvass[xb-i, ya+i]+=1   
        else:
            print(f"NO MATCH: ({x1},{y1}) -> ({x2},{y2})") 
    #print(canvass.transpose())            
    return len(np.where(canvass >= 2)[0]) 

print(get_count_two_lines(test_data,test_br))
print(get_count_two_lines(data, br))    