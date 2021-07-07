fruits=['apple','kiwi','orange','banana']
with open('test.txt', "w") as f:
    for i in range(fruits):
        f.write("%s\n" % i)
text=open('test.txt')
print(text.read())