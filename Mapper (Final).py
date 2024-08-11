#!/usr/bin/env python3
import sys
import csv
import re

#Preprocess the text
def preprocess_text(text):
    text = re.sub(r'\d+', '', text)
    text = text.replace('_', ' ') #Replace underscores and leave a space
    text = re.sub(r'[^\w\s]', ' ', text) #Remove special characters and leave a space
    text = text.lower() #Change to lowercase
    return text

#Read from standard input
reader = csv.reader(sys.stdin)
header = next(reader, None)  #Skip header

for row in reader:
    if len(row) >= 10:  #Check if columns are 10
        review_text = row[9]  #Pinpoint the specific review_text column for processing
        processed_text = preprocess_text(review_text) #Processess the review column
        tokens = processed_text.split()  #Tokenise it
        for token in tokens:
            if token:
                print (f'{token}\t1')