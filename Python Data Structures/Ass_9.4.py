'''9.4 Write a program to read through the mbox-short.txt
and figureout who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates
a Python dictionary that maps the sender's mail address to a count of
the number of times they appear in the file. After the dictionary
is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
f = open(name)
count = dict()
emails = []
for line in f:
    if line.startswith('From '):
        words = line.split()
        #print(words[1])
        count[words[1]] = count.get(words[1],0)+1
#print(count)
highestNum = None
highestItem = None
for k,v in count.items():
    if highestNum < int(v) or highestNum == None:
        highestNum = v
        highestItem = k
print(highestItem,highestNum)    
