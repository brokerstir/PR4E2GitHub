import re
fname = raw_input("Enter file name: ") # ask user for file
lines = open(fname) # read data
numberList = list() # create empty list
for line in lines: # loop through lines
    line = line.rstrip() # strip whitespace
    numberString = re.findall('[0-9]+', line) # extract strings of digits to a list
    for x in numberString: # loop through the strings of digits list
        number = int(x) # convert strings of digits to integers
        numberList.append(number) # add integers to number list
sum = 0 # declare a variable       
for i in numberList: # loop through list of integers
    sum += i # calculate sum of integers
print sum # print the sum