with open('test.txt') as f:
    text=f.read.split()
print(max(text, key=len))