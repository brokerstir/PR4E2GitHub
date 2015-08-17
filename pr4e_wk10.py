name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)

# Loop through the text, find lines that start with "From ", 
# split the line to words or elements, then put the fifth element of each line
# into a list of times
times = list()
for line in fhandle:
    if not line.startswith("From ") : continue
    if line.startswith("From ") :
        line = line.rstrip() #strips white space
        elements = line.split()
        time = elements[5]
        time = time[:2]
        times.append(time)
        
# Here we create a dictionary using our list of times, and count them 
# The dictionary will count the occurence of each hour       
hours = dict()
for hour in times:
    hours[hour] = hours.get(hour,0) + 1

# Sort the dictionary into and ordered list of tuples, and then print
hrFrequency = list()
for key, val in hours.items():
    hrTupl = (key, val)
    hrFrequency.append(hrTupl)
hrFrequency.sort()
    
for key, val in hrFrequency:
    print key, val
