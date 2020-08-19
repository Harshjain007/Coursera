
'''Extracting Data With Regular Expressions'''
import re
fname = input("Enter file:")
if len(fname) < 1 : fname = "regex_sum_458422.txt"
handle = open(fname)
numlist = list()
for line in handle:
    stuff = re.findall('[0-9]+', line)
    numlist = numlist + stuff

sum = 0
for i in numlist:
    sum = sum + int (i)
print(sum)
