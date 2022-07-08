
"""
Sentiment analysis using links from google, backend of google sentiment extension.
"""

# Imports
import sys
import os

# Data handling
import pandas as pd 

# Sentiment analysis
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

# Path declaration
curpath = os.path.abspath(os.curdir)

# Function declarations

# Performs sentiment analysis using TextBlob, prints results
def sent_textblob(Articles):
    nArticles = len(Articles)
    
    for i in range(nArticles):
        currArticle = Articles[i]
        print("\n the sentiment of article", i," \n ", "\"", currArticle, "\"" , "\n is:", TextBlob(currArticle).sentiment)

# Performs sentiment analysis on a list of input links
def sentiment_analysis(input_links):
    df1 = pd.DataFrame()
    
    # input articles into pandas DataFrame
    counter = 0
    for link in input_links:
        # stub, input scraping function here. probably gonna use beautifulsoup.
        df1.at[counter, 'Article'] = "good" + " " + str(counter)
        df1.at[counter, 'Link'] = link
        counter += 1
    
    # make every word lowercase
    df1['lowercase'] = df1['Article'].apply(lambda x: " ".join(word.lower() for word in x.split()))
    
    # remove any puctuation
    df1['punctuation'] = df1['lowercase'].str.replace('[^\w\s]', '', regex=True)
    
    # remove stopwords
    stop_words = stopwords.words('english')
    df1['stopwords'] = df1['punctuation'].apply(lambda x: " ".join(word for word in x.split() if word not in stop_words))
    
    # lemmatize 
    df1['lemmatized'] = df1['stopwords'].apply(lambda x: " ".join(Word(word).lemmatize() for word in x.split()))
    
    # calculate sentiment
    df1['polarity'] = df1['lemmatized'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df1['subjectivity'] = df1['lemmatized'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    
    return df1
    


def main():
    # args = sys.argv[1:]
    test_links = ["www.google.com", "www.cnn.com", "www.facebook.com"]
    df1 = sentiment_analysis(test_links)
    
    print(df1)
    
    
# Main body
if __name__ == '__main__':
    main()
    
    
 
        
            
        