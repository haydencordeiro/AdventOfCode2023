ip = [
]

# Open the file in read mode
with open('task1.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    ip = file.readlines()



def getFirstNumer(i):
    for j in i:
        if j.isnumeric():
            return j
    
def getLastNumer(i):
    for j in i[::-1]:
        if j.isnumeric():
            return j
total = 0    
for i in ip:
    first = getFirstNumer(i)
    last = getLastNumer(i)
    total += int(first + last)

print(total)
