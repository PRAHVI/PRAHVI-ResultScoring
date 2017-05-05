#!/usr/bin/python3

import argparse
from fuzzywuzzy import fuzz

def getScore(fileAName, fileBName):
	with open (fileAName, "r") as fileA:
		textA = fileA.read().replace('\n', '')

	with open (fileBName, "r") as fileB:
		textB = fileB.read().replace('\n', '')

	return fuzz.partial_ratio(textA, textB)


parser = argparse.ArgumentParser()

parser.add_argument("fileA", help='path for first file')
parser.add_argument("fileB", help='path for second file')
args = parser.parse_args()
print(getScore(args.fileA, args.fileB))