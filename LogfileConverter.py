#!/usr/bin/env python3

# For trying to make it accept a drag and dop file.
# import sys
# fileIn = sys.argv[1]

def main():
	rawData, fName = getFileIn()

	out = "{}.log"
	f2 = open(out.format(fName), "w") # Name new file same as old one.

	sizeOfData = 200 # This is the size of one set of data

	for i in range(int(len(rawData)/sizeOfData)): # Divide file content into n sets of data
		j = i*sizeOfData
		f2.write(rawData[j:(j+(sizeOfData-1))]+"\n") # Step through one set at a time
		# if i > 2: break # For quick testing purposes
	f2.close()


def getFileIn():
	while True:
		try:
			fileIn = input("Paste filename with extension: ")
			f1 = open(fileIn, encoding ='ISO-8859-1') # Need this encoding or raw files won't open
			break
		except FileNotFoundError:
			print("File not found: Check the name is correct and that it's in the same location as the script.")

	fName = f1.name[:f1.name.find(".")] # Take filename without extension to make matching output file
	rawData = f1.read()
	f1.close()
	return rawData, fName

main()





