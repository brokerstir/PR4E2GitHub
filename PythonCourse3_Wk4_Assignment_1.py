# Welcome robert risk from Using Python to Access Web Data

# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.pythonlearn.com/code/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html (Sum=2553)
# Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174675.html (Sum ends with 12)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
# Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.

# ...
# Retrieve all of the anchor tags
## tags = soup('a')
# for tag in tags:
   # Look at the parts of a tag
   ## print 'TAG:',tag
   ## print 'URL:',tag.get('href', None)
   ## print 'Contents:',tag.contents[0]
   ## print 'Attrs:',tag.attrs
# You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the span tags
# Each tag is like a dictionary of HTML attributes

tags = soup('span')

sum = 0
for tag in tags:
    number = tag.text
    number = int(number)
    sum = sum + number
print sum

#    tag = tag.rstrip() # strip whitespace
#    numberString = re.findall('[0-9]+', tag) # extract strings of digits to a list
#    print numbertring
#print numberstring
#    for x in numberString: # loop through the strings of digits list
#        number = int(x) # convert strings of digits to integers
#        numberList.append(number) # add integers to number list
#sum = 0 # declare a variable       
#for i in numberList: # loop through list of integers
#    sum += i # calculate sum of integers
#print sum # print the sum



 
