# Use the file name mbox-short.txt as the file name
# Prompt user for a file and create a handle for the file
fname = raw_input("Enter file name: ")
fh = open(fname)
# Define needed variables
count = 0
sum = 0
avg = 0
# Loop through the file to look for desired data and compute average
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1
        pos = line.find(":")
        num = float(line[pos+1:]);
        sum += num
    avg = float(sum / count);
# Print the average
print "Average spam confidence:", avg
