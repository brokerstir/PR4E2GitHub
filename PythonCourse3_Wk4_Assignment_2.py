# Welcome robert risk from Using Python to Access Web Data

# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Shantelle.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: E
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

# Sample execution

# Here is a sample execution of a solution:

# $ python solution.py 
# Enter URL: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Fikret.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Montgomery.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Mhairade.html
# Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Butchi.html
# Last Url: http://pr4e.dr-chuck.com/ ... /known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Shantelle.html' # define first url
count = 0 # define count variable
print url # prints the first url
while count < 7: # loop through process 4 times
    position = 0 # define position
    html = urllib.urlopen(url).read() # open html page
    soup = BeautifulSoup(html) # convert to soup
    count += 1 # increment count
    tags = soup('a') # retrieve all of the anchor tags
    for tag in tags: # loop through anchor tags  
        url = tag.get('href', None) # set url to the anchor tag
        position += 1 # increment position
        if position == 18:
            print url # print url if at positon 3
            break # jumps out of for loop
  
