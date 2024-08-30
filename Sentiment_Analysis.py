import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

class Sentiment_Analysis:
    def __init__(self):
        self.token = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.sentiments = ['Negative','Neutral','Positive']
        
    def preprocess_text(self,text):
        text = str(text)
        text = text.lower()
        text = re.sub(r'https?://\S+|www\.\S+|\[.*?\]|[^a-zA-Z\s]+|\w*\d\w*', ' ', text)
        text = re.sub(r'\n', ' ', text)

        stop_words = set(stopwords.words("english"))
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        text = ' '.join(filtered_words).strip()

        tokens = nltk.word_tokenize(text)

        lemmatizer = WordNetLemmatizer()
        lem_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        return ' '.join(lem_tokens)


    def sentiment_analyse(self,text):
        out = self.token(text,return_tensors='pt')
        out = self.model(**out)
        score = out[0][0].detach().numpy()
        score = list(softmax(score))
        return score.index(max(score)),max(score)
    
    def start(self,df):
        df = df.dropna()
        df.columns = ["Review"]
        data = []
        count_positive = 0
        count_negative = 0
        count_neutral = 0
        sentiments = []
        score = 0
        for i in df.iterrows():
            rev = list(i[1])[0]
            if rev == '':
                continue
            data.append(rev)
            try:
                rev = rev[:1500]
            except:
                pass
            res,v = self.sentiment_analyse(rev)
            sentiments.append(self.sentiments[res])
            if res==0:
                count_negative+=1
                score -= v
            elif res==1:
                count_neutral+=1
                score += v/2
            else:
                count_positive+=1
                score += v
        
        d = []
        c = 0
        for i,j in list(zip(data,sentiments)):
            d.append({'review':i,'rating':j})
            c += 1
            if c == 50:
                break

        score = (score/(count_positive+count_negative+count_neutral)) * 100
        
        return {'counts': [count_positive, count_negative, count_neutral], 'data':d,'score':score}

        
if __name__ == '__main__':
    obj = Sentiment_Analysis()
    print(obj.start(pd.read_csv('reviews.csv')))

