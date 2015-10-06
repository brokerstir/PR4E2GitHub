 # Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
 
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fhandle = open(fname) #read data
words = list()
emails = dict() #create empty dictionary
for line in fhandle:
    if not line.startswith('From ') : continue #skip lines not starting with From
    row = line.rstrip() #strip every line of whitespace
    words = row.split() #make every line a list of words
    emails[words[1]] = emails.get(words[1], 0) + 1

mostcount = None
mostemail = None #intialize variables
for email,count in emails.items(): #loop through key-value pairs in dictionary
    if mostcount is None or count > mostcount: #find and assign the most prolific commiter
        mostemail = email
        mostcount = count 
print mostemail, mostcount