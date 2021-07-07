with open("test.txt", "w") as f:
    f.write("Almaty city\n")
    f.write("Happy")
text=open("test.txt")
print(text.read())