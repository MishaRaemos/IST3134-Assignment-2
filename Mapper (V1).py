#!/usr/bin/env python3
import sys
import csv

#Uses the CSV reader
reader = csv.reader(sys.stdin)

# Skip header if it exists
header = next(reader, None)  #If there’s no header, none is used to handle it, and it is skipped

for row in reader:
    if len(row) >= 10:  #Targeting review summary and review test for pre-proccessing
        review_summary = row[8]
        review_text = row[9]
        words = review_summary.split() + review_text.split()
        for word in words:
            word = word.strip().lower()  #Change to lowercase and remove whitespaces
            if word:  #Ignore empty words
                print (f'{word}\t1')
