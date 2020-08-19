'''
9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages. The program
looks for 'From ' lines and takes the second word of those lines as the person
who sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in
the file. After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : fname = 'mbox-short.txt'
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()                                                 
    if not 'From:' in line :
        continue
    words = line.split("from:")
    words = line[6:]
    counts[words] = counts.get(words,0) + 1
                                
large = -1
mail = None             
for aaa, bbb in counts.items():
    if bbb > large :
        large = bbb
        mail = aaa
print(mail, large )
'''                                                  #   print(key, counts[key])

keymax = max(counts, key=counts.get)
print(keymax, counts[keymax])
'''

'''
Output:
cwen@iupui.edu 5
'''
