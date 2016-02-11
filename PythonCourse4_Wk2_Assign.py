## Welcome robert risk from Using Databases with Python

## To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
## Choose File
##(Must have a .sqlite suffix)
## Hint: The top organizational count is 536.
## Submit
## You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

## Counting Organizations
## This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

## CREATE TABLE Counts (org TEXT, count INTEGER)
## When you have run the program on mbox.txt upload the resulting database file above for grading.
## If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

## You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py. The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

import sqlite3

# connect to database and set a cursor
conn = sqlite3.connect('domaindb.sqlite')
cur = conn.cursor()

# drop existing table named Counts, if it exists
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# create table named Counts, with two columns - org and count
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# get file name from user or choose default file, then creat a handle to open file
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)

# loop through every line in file
for line in fh:
    if not line.startswith('From: ') : continue # jump out of current iteration
    ##line = line.rstrip()
    ##line = str(line)
    ##position = line.find('@')
    ##end = line.find(' ',position)
    ##domain = line[position+1:end+1]
    
        
    pieces = line.split() # split line into separate strings
    email = pieces[1] # set variable name for second string in line
    email_split = email.split('@') # split the second string into substrings
    domain = email_split[1] # set variable for second substring
    
    
    ##cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    # select row in table with defined domain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))
    row = cur.fetchone()
    
    # if domain does not exsit in a row yet, set that domain in the org column with a count of 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( domain, ) )
                
    # that domain does exist in a row already so increment org count
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (domain, ))
    conn.commit() # write to database

# https://www.sqlite.org/lang_select.html

# select top ten databse entries by count, in descending order
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# print both columns in top ten rows
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

# close database connection
cur.close()


