n=int(input())
with open("test.txt") as f:
    for line in (f.readlines() [-n:]):
        print(line)