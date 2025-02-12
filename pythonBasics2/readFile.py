
file = open("test.txt")

#print(file.read())      #read all content of file
#print(file.read(5))       #if want to read n number of character

# print(file.readline())   #read first line of file
# print(file.readline())      #read second line of file

#print line by line using readline method
# line = file.readline()
# while line != "":               #read until blank line
#     print(line)
#     line = file.readline()


for line in file.readlines():
    print(line)

file.close()        #good practice close file