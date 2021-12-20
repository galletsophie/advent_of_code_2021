import pandas as pd
import numpy as np

data= pd.read_csv("day8.csv", header=None)

small_test = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |cdfeb fcadb cdfeb cdbaf"""

large_test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce"""


def compute_easy_count_test(several_rows):
    in_out = several_rows.split("\n")
    easy_count = 0
    for output in in_out[1::2]: #skip input
        output_list = output.split(" ")
        easy_count += sum([1 for e in output_list if len(e)<=4 or len(e)==7])
    return easy_count

def compute_easy_count(df):
    out_col = df[0].str.split("|", expand=True)[1]
    easy_count = 0
    for output in out_col:
        output_list = output.split(" ")[1:] #first elt is an empty string, slice to remove it
        easy_count += sum([1 for e in output_list if len(e)<=4 or len(e)==7])
    return easy_count

#print(compute_easy_count_test(large_test))
#print(compute_easy_count(data))

#--- Part Two ---
def decode_one_line(in_n_out_str):
    # Initialize and prep data
    nb_codes = [0]*10

    input_str, output_str = in_n_out_str.split(" |")
    input_list_of_list = [sorted(list(c)) for c in input_str.split(" ")]
    output_list_of_list = [sorted(list(c)) for c in output_str.split(" ")]

    # MAP INPUT 
    ## Easy numbers
    nb_codes[1] =[e for e in input_list_of_list if len(e)==2][0]
    nb_codes[7] = [e for e in input_list_of_list if len(e)==3][0]
    nb_codes[4] = [e for e in input_list_of_list if len(e)==4][0]
    nb_codes[8] = [e for e in input_list_of_list if len(e)==7][0]

    ## Deduction part
    len5_nb = [e for e in input_list_of_list if len(e)==5] #2,3,5
    len6_nb = [e for e in input_list_of_list if len(e)==6] #0,6,9

    # #3: only 5-segment nb that includes 1
    nb_codes[3] = [e for e in len5_nb if nb_codes[1][0] in e and nb_codes[1][1] in e ][0] 
    len5_nb = [e for e in len5_nb if e != nb_codes[3]]
    # #9: only 6-segment nb that includes 3
    nb_codes[9] =[e for e in len6_nb if len(set(nb_codes[3]) & set(e))==5][0]
    len6_nb = [e for e in len6_nb if e != nb_codes[9]] 
    # #5: only remaining 5-segment nb with 5 segments in commmon with #9
    nb_codes[5] =[e for e in len5_nb if len(set(nb_codes[9]) & set(e))==5][0]
    nb_codes[2] = [e for e in len5_nb if e != nb_codes[5]] [0]   
    # #6: only 6-segment nb with 5 segments in commmon with #5
    nb_codes[6] =[e for e in len6_nb if len(set(nb_codes[5]) & set(e))==5][0]
    nb_codes[0] = [e for e in len6_nb if e != nb_codes[6]][0]
    
    # DECODE OUTPUT
    decoded_output = ''
    #for e in output_list_of_list[1:]: #this works for small_test
    for e in output_list_of_list[1:]:
        decoded_output+= str([i for i,code in enumerate(nb_codes) if e == code][0])
    return int(decoded_output)

def decode_all(df):
    output_sum = 0
    for row in df[0]:
        decoded_nb = decode_one_line(row)
        output_sum+=decoded_nb
    return output_sum

output_sum = decode_all(data)   
print(output_sum)