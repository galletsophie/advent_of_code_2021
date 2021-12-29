from enum import auto
from os import error
import pandas as pd
import re
from statistics import median 

test = pd.read_csv("day10_test.csv", header=None, names=["code"])["code"]
data = pd.read_csv("day10.csv", header=None, names=["code"])["code"]

error_points = {')': 3, ']':57, '}':1197, '>':25137}
error_counts = {')':0, '}':0,']':0,'>':0}

ch_list = [')','}',']','>']

def cleanup(row):
    # Remove couples of consecutive characters recursively 
    newrow = row.replace('()','').replace('<>','').replace('[]','').replace('{}','')
    if newrow == row:   
        return newrow
    else:
        return cleanup(newrow) 

def is_incomplete(cleaned_row):
    # Return Bool, True if no closing characters in cleaned row
    closing_occurences = 0
    for ch in ['\)', '}', ']', '>']:
        closing_occurences += len(re.findall(ch, cleaned_row))
    return closing_occurences == 0  


def find_offending_ch(cleaned_row):
    if not is_incomplete(cleaned_row):
        # find first closing character
        locs = [cleaned_row.find(ch) for ch in ch_list]
        offending_loc = min([e for e in locs if e != -1])
        offending_ch = cleaned_row[offending_loc]
        # increment error count
        error_counts[offending_ch]+=1
        return None

def main(data):
    total = 0
    for row in data:
        cleaned_row = cleanup(row)
        if not is_incomplete(cleaned_row):
            find_offending_ch(cleaned_row)
    for k in error_counts.keys():
        total += error_counts[k] * error_points[k]
    return total
print(main(data))    

# --- Part Two ---
auto_complete_points = {'(':1, '[':2, '{':3, '<':4}

def find_closing_seq_score(cleaned_row):
    score = 0
    for ch in cleaned_row[::-1]: #loop in reverse order
        score *= 5
        score += auto_complete_points[ch]
    return score    

def main(data):
    total = []
    for row in data:
        cleaned_row = cleanup(row)
        if is_incomplete(cleaned_row):
            score = find_closing_seq_score(cleaned_row)
            total.append(score)
    return median(total)
print(main(data)) 