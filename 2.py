n=int(input())
with open("test.txt") as f:
    text=[next(f) for i in range(n)]
print(text)