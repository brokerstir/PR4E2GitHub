#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

#Get file name from user.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
#Read the file.
fhandle = open(name)
#Create empty dictionary.
hours = list()
#Loop through every line in file and split the words.
for line in fhandle:
    if not line.startswith('From ') : continue #skip lines not starting with From
    row = line.rstrip() #strip every line of whitespace
    words = row.split() #make every line a list of words
    hour = words[5] #get the sixth word in the line
    hour = hour[0:2] #split the word to save only the hour
    hours.append(hour) #add hour to list of hours
    
hour_counts = dict() #create empty dictionary
for hour in hours: #loop through hours and build dictionary that counts occurence of each hour
    hour_counts[hour] = hour_counts.get(hour, 0) + 1

#creat a sorted tuple by looping through dictionary    
counts = sorted( [(k, v) for k, v in hour_counts.items()] )
for k, v in counts: #print sorted tuples
    print k, v
    



    
    