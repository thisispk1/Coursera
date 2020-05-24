name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

hours = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()

    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0],0) + 1

lst = []

for a,b in hours.items():
    lst.append((a,b))

lst.sort()


for a,b in lst:
    print (a,b)