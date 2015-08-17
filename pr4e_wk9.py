name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# Lines 8-15 will loop through the text, find lines that start with "From ", 
# split the line to words or elements, then put the second element of each line
# into a list of emails
emails = list()
for line in handle:
    if not line.startswith("From ") : continue
    if line.startswith("From ") :
        line = line.rstrip() #strips white space
        elements = line.split()
        email = elements[1]
        emails.append(email)

# Here we create a dictionary using our list of emails, and count the occurrences        
edict = dict()
for eaddy in emails:
    edict[eaddy] = edict.get(eaddy,0) + 1
    
# Here we create a loop to find the email with the max number of sends
maxemail = None
maxsends = None
for email,sends in edict.items():
    if maxsends == None or maxsends < sends :
        maxemail = email
        maxsends = sends
        
print maxemail, maxsends