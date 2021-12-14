#!/usr/bin/env python3
import sys

# fileIn = sys.argv[1]

print("RUNNING")

def main():
	rawData, fName = getRaw()

	out = "{}.log"
	f2 = open(out.format(fName), "w")

	sizeOfData = 200 # This is the size of one set of data

	for i in range(int(len(rawData)/sizeOfData)): # Divide file content into n sets of data
		j = i*sizeOfData
		f2.write(rawData[j:(j+(sizeOfData-1))]+"\n") # Step through one set at a time
		# if i > 2: break # For quick testing purposes
	f2.close()


def getRaw():
	fileIn = input("Paste filename with extension: ")
	# fileIn = sys.argv[1]
	f1 = open(fileIn, encoding ='ISO-8859-1') # Need this encoding or raw files won't open
	fName = f1.name[:f1.name.find(".")] # Take filename without extension to make matching output file
	rawData = f1.read()
	f1.close()
	return rawData, fName

main()





