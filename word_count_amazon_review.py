# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 07:27:56 2024

@author: User
"""

import pandas as pd
import re
from collections import Counter
import time

input_path = r'C:\Users\User\Downloads\Books_rating.csv'
output_path = 'word_count2.txt'
df = pd.read_csv(input_path)

#Starting the timer of the code
start_time = time.time()
#Combining all the words columns into a string
all_reviews = ''.join(df['review/text'].astype(str))
#Tokenizing the sentence to individual words
words = re.findall(r'\b\w+\b', all_reviews.lower())
#Counting the number of words
word_count = Counter(words)
#Ending the timer of the code
end_time = time.time()
#calculating the total time taken in milliseconds
total_time_ms = (end_time - start_time) * 1000

#Printing the time taken for word count process 
print(f"Word counting process completed in {total_time_ms:.2f} ms.")
#Outputting the word counts into txt file
with open(output_path, 'w') as file:
    for word, count in word_count.most_common():
        file.write(f"{word}: {count}\n")
        
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Read the text file
def read_word_counts(output_path):
    word_counts = {}
    with open(output_path, 'r') as file:
        for line in file:
            word, count = line.strip().split(': ')
            word_counts[word] = int(count)
    return word_counts

# Classify words into positive, negative, and neutral sentiment
def classify_sentiments(word_counts):
    analyzer = SentimentIntensityAnalyzer()
    pos_words = {}
    neg_words = {}
    neu_words = {}
    for word, count in word_counts.items():
        sentiment_score = analyzer.polarity_scores(word)['compound']
        if sentiment_score > 0:
            pos_words[word] = count
        elif sentiment_score < 0:
            neg_words[word] = count
        else:
            neu_words[word] = count
    return pos_words, neg_words, neu_words

# Read the word counts
word_counts = read_word_counts(output_path)

# Classify words into positive, negative, and neutral sentiments
pos_words, neg_words, neu_words = classify_sentiments(word_counts)

# Create word clouds for positive, negative, and neutral words
wordcloud_pos = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate_from_frequencies(pos_words)
wordcloud_neg = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate_from_frequencies(neg_words)
wordcloud_neu = WordCloud(width=800, height=400, background_color='white', colormap='Blues').generate_from_frequencies(neu_words)

# Plot the word clouds
plt.figure(figsize=(10, 10), dpi = 150)
plt.subplot(1, 3, 1)
plt.imshow(wordcloud_pos, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Sentiment Word Cloud')
plt.show()  

plt.subplot(1, 3, 2)
plt.imshow(wordcloud_neg, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Sentiment Word Cloud')
plt.show()  

plt.subplot(1, 3, 3)
plt.imshow(wordcloud_neu, interpolation='bilinear')
plt.axis('off')
plt.title('Neutral Sentiment Word Cloud')
plt.show()        
