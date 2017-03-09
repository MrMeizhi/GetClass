#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib

def main():

	sourceFile = raw_input("Type your source file name:")

	saveFile = raw_input("Type your save file name:")

	resultFile = open(saveFile,'a+')
	
	with open(sourceFile) as allLines:

		for line in allLines:

			getOneLine = line.split('\t')

			resultLine = getOneLine[0] + '_' + getOneLine[1] + '_' + getOneLine[3]

			resultLine = urllib.quote(resultLine)

			resultFile.write(resultLine.lower() + '\n')

	resultFile.close()


if __name__ == '__main__':
	main()