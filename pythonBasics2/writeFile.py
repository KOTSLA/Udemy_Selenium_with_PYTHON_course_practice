# file = open("test.txt")
# file.close()


#another way to open file, without closing it
with open("test.txt", "r") as reader:       #read from file index r
    content = reader.readlines()
    reversed(content)
    with open("test.txt", "w") as writer:       #write to file index w
        for line in reversed(content):
            writer.write(line)

