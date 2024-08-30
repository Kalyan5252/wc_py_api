from Extraction import Review_Price_Extract
from Fake_Review_Detector import Fake_Review_Analysis
from Sentiment_Analysis import Sentiment_Analysis

import string,nltk,pickle
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import re
from amazoncaptcha import AmazonCaptcha

from summarizer import SummarizeProduct


from time import time,sleep
def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

class Feature1:
    
    def __init__(self):
        self.extracter = Review_Price_Extract()
        self.detector  = Fake_Review_Analysis()
        self.sentiment = Sentiment_Analysis()
        
    def start(self,link):
        self.extracter.start()
        
        reviews = self.extracter.review_extract(link)
        total_reviews_count = len(reviews)
        
        price_result = self.extracter.price_analysis(link)
        
        self.extracter.stop()
        
        geniune_reviews = self.detector.filter(reviews)
        geniune_reviews_count = len(geniune_reviews)
        geniune_reviews.columns = ['Reviews']
        print(' '.join(list(geniune_reviews['Reviews'])))
        sleep(1)
        r = SummarizeProduct(' '.join(list(geniune_reviews['Reviews'])))
        sleep(1)
        sentiment_report = self.sentiment.start(geniune_reviews)
        
        
        return [price_result,sentiment_report,r]

def Analysis(link):
    # t = time()
    obj = Feature1()
    return obj.start(link)
    # return obj.start('https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHWV2WYK/ref=sr_1_3?sr=8-3')
        

        
        
        
        
        