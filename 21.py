import string
def letters_file_line(n):
    with open("words.txt", "w") as f:
        alphabet=string.ascii_uppercase
        letters=[alphabet[i:i+n]+"\n" for i in range(0, len(alphabet),n)]
        f.writelines(letters)
