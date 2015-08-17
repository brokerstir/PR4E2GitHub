fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    if line.startswith("From ") :
        count += 1
        line = line.rstrip()
        elements = line.split()
        print elements[1]
print "There were", count, "lines in the file with From as the first word"