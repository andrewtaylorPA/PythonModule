#  Exception Handling

#
"""
try:
    #code to try
    pass
except:
    #code that runs if it fails

"""

try:
    textfile = open('testfile.txt')
    print("This file exists")
    textfile.close()
except Exception as e:
    print("It failed due to:", e) # e is the error variable
    textfile = open('testfile.txt','w')
    textfile.close()
    print("Created text file")