counter=0
with open('test.txt') as f:
    lines=f.readlines()
    for Line in range(lines):
        counter+=1
print(counter)