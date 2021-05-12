#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
gets = 0
posts = 0
logins = 0
# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
# loop over the list of lines
for line in keystone_file_lines:
    # if this 'fail pattern' appears in the line...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
    if "GET" in line:
        gets += 1
    if "POST" in line:
        posts += 1
    if "-] Authorization failed" in line:
        logins += 1
print("The number of failed log in attempts is", loginfail,"\n Total GET", gets, "\n Total POST" , posts, "\nSuccessful logins", logins)
keystone_file.close() # close the open file

