arr=[]
with open('test.txt') as f:
    lines=f.readlines()
    for line in range(lines):
        arr.append(line)
print(arr)