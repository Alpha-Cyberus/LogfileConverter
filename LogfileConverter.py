import sys

# fileIn = input("Paste filename with extension: ")
fileIn = sys.argv[1]
fName = fileIn
print(fName)
# Test Comment
f1 = open(fileIn, encoding ='ISO-8859-1')
rawData = f1.read()
f1.close()

f2 = open("./results.log", "w")

for i in range(int(len(rawData)/200)):
	j = i*200
	f2.write(rawData[j:(j+199)]+"\n")
	# if i > 2: break

f2.close()

# f2 = open("./results.log")
# print(f2.read())






