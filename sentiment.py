# Imports
import sys
import os

# Data handling
import pandas as pd 

# Sentiment analysis
from textblob import TextBlob
from nltk.corpus import stopwords


def main():
    args = sys.argv[1:]
    
    sentence = "School is great"
    bad_sentence = "I hate school"
    
    print("The sentiment of\" ", sentence, "\" is: ", TextBlob(sentence).sentiment.polarity)
    print("The sentiment of\" ", bad_sentence, "\" is: ", TextBlob(bad_sentence).sentiment.polarity)


# Main
if __name__ == '__main__':
    main()
    
   
        
            
        