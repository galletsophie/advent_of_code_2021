import pandas as pd


#--- Part One ---
data = pd.read_csv('day2.csv', header=None, names = ['directions'])

# Split into 2 columns, change type to int
data[['direction', 'quantifier']] = data['directions'].str.split(' ', 1, expand=True)
data.drop('directions', axis=1, inplace=True)
data.quantifier = data.quantifier.astype('int')

depth = 0
position = 0

for (dir, qtfier) in data.itertuples(index=False):
    if dir == 'forward':
        position += qtfier
    elif dir == 'down':
        depth += qtfier
    else:
        depth -= qtfier    

#print(position, depth, position * depth)

#--- Part Two ---
def compute_finalmultiplication(data):
    aim = 0
    depth = 0
    position = 0

    for (dir, qtfier) in data.itertuples(index=False):
        if dir == 'forward':
            position += qtfier
            depth += aim * qtfier
        elif dir == 'down':
            aim += qtfier
        else:#up
            aim -= qtfier 

    return depth*position

test_df = pd.DataFrame({'directions': ['forward', 'down', 'forward', 'up', 'down', 'forward'],
                        'quantifier':[5,5,8,3,8,2]})
test_dp = compute_finalmultiplication(test_df)
data_dp = compute_finalmultiplication(data)
print(test_dp)
print(data_dp)