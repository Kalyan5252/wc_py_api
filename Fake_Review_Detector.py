from joblib import load
import pandas as pd
import string,nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

class Fake_Review_Analysis:
    
    def __init__(self):
        self.model = load(open(r"fake_review.joblib", 'rb'))

    def filter(self,df):
        l=[]
        df.dropna()
        df.columns = ['Reviews']
        for index, row in df.iterrows():
            
            if str(row['Reviews']) == 'nan':
                continue
            row_series = pd.Series(row)
            prediction = self.model.predict(row_series.values.reshape(1, -1))[0]
            if prediction == "OR":
                l.append(row['Reviews'])
        return pd.DataFrame(l,columns=['Reviews'])
        

if __name__ == '__main__':
    o = Fake_Review_Analysis()
    print(o.filter(pd.read_csv('reviews.csv')))