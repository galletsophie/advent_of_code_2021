import pandas as pd



# Part 1 
data = pd.read_csv('day1.csv', header=None, names = ['readings'])

prev_reading = max(data.readings) #first mistake initializing at 0.. 
increase_count = 0 

for reading in data.readings:
    if reading > prev_reading: #assuming strictly larger, but same result anyway
    #if reading >= prev_reading:  
        increase_count +=1 
    prev_reading = reading

#print(increase_count)    

# Part 2 

prev_sum = 3*max(data.readings)
rolling_increase_count = 0

# the easy way
rolling_sums = data.readings.rolling(3).sum() #that didn't work out as expected
for r_sum in rolling_sums:
    if r_sum > prev_sum:
        rolling_increase_count+=1
    prev_sum = r_sum 

print(rolling_increase_count)

# initially thought above was wrong so I reimplemented it myself -- tired 
rolling_increase_count = 0
for i, reading in enumerate(data.readings):
    r_sum = data.readings[i:i+3].sum()
    if r_sum > prev_sum:
        rolling_increase_count+=1
    prev_sum = r_sum    

print(rolling_increase_count)   