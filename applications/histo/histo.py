# Your code here

robin = open("applications/histo/robin.txt",'r').read()

box = robin.replace(',','')

box = box.replace('.','')

box = box.replace('"','')

box = box.replace('!','')

box = box.replace('?','')

box = box.replace(";",'')

box = box.replace(":",'')

box = box.lower()

box = set(box.rsplit())

longest = 0

for x in box:
    if longest < len(x):
        longest = len(x)

print(longest)


container = {}


for x in box:
    container[x] = robin.lower().count(x) * '#'

for x in container:
    print(f"{x}:".ljust(longest+2),f"{str(container[x])}")

