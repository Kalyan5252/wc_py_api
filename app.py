from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from summarizer import SummarizeProduct
from chatbot import ChatBot
from feature1 import Analysis

from Extraction import Review_Price_Extract
from Fake_Review_Detector import Fake_Review_Analysis
from Sentiment_Analysis import Sentiment_Analysis
from amazoncaptcha import AmazonCaptcha

import string,nltk,pickle
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import re

ob = ChatBot()

app = Flask(__name__)
CORS(app)

def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


@app.route('/summarizeProduct',methods =['POST'])
def summarize():
    # st = request.form.get('prompt')
    st = request.json['prompt']
    # print(st)
    # st = """Battery backup is so good . It can last up to above 1 day if the user has normal usage like social media apps and Content watching apps like YouTube Facebook Netflix Instagram. Smoothness of the Screen is very good . Day to day use is very good . User should not feel any lag . 5G Connectivity is very helpful. Apps takes less time to download, they download very fast. Call quality is superb , Clear and high quality sound when calling to someone if person is indoor or outdoor. In both condition multimedia and call quality is👍👍. But camera is okkish I must say not too good not very bad . ok ok . Black colour is good from my point of view if want to purchase this mobile . Battery Call quality and screen smoothness is top notch in this price segment. If want to purchase this mobile I must say you should go with that . Specially if person wants good battery backup and sound quality. Rest every person has its own choice and budget. It is my First ONE PLUS purchase. I am using it from last 20 days I have not feel any Heating issue. Because i have said I am not heavy user that why I have not feel any Heating of laggs. Phones comes with 80 Watts vooc charger which charges the phone very fast. Battery life great, Good fast charging, display lcd but 120hz ok enough, little heavy weight, fast storage, minimal heating, good for casual gaming, processor okk okk, camera is very average not impressive Very good phone under Rs 20000, i bought this last June 2023, working well with superb battery backup, awesome camera, ultrafast charging One plus CE3 lite.. What a brilliant concept.. I loved it.. Super display quality.. Best battery backup.. Fast charging with 80w... Superb performance.. Very smoothly working pubg game.. And camera is ok from this price.. Totally i love this one plus phone... Thanks🤩 Phone is too good..battery, camera,sound,touch.everytjing is too good..just go for it.. The camera is really bad, all the features and sound is beautiful, not sure why one plus made a blunder in especially the camera!Charging is really fast and stays all dayDoesn't heat much only while charging.Weight seems to be ok the feel/grip is greatReally good sensor, just a tap unlocks the phoneScreen is really clear. I bought this phone for my father, who wanted under budget phone. It is a good phone with long battery. Just that touch is not very swift and can contains only limited apps. It does says as per its specifics, but camera quality could be improved better. The camera flash is not so good. Pros about Nord CE 3 Lite : Look and operation wise is absolutely fine.Cons about Nord CE 3 Lite:1. Camera Quality is very poor.2. Battery draining very quickly. Even If I browse facebook/instagram/whatsapp, battery drains quickly. My earlier mobile is better than this mobile.3. 80 W is mentioned / printed on the charger adaptor. Actually it is 67 W. However, before purchase it was clearly mentioned as of 67 W only. By mistake, it might have mentioned on the charger. Or any other specification??4. Alarm sound very low5. Mobile heat up if we use continuously. I am writting this review after using the phone for more than a year. My satisfaction level is quite high for this phone. The built of mobile is so good. Look wise it is quite trendy. Performance is excellent. Quality of camera is very good. It comes with a super chager. Charging time of the mobile is very less. Back up is nice. After all it's a crafted mobile. It's worth every penny you spent .I have only small issues regarding the sound quality. When connected to bluetooth the sound is very low even at maximum volume.I specifically want to mention about it's water resistance quality. 'Marvellous' is what I would like to mention about it's resistivity towards ingress of water. My mobile fell down in water and remained under water for nearly 6 hours. When recovered, I was surprised to see the mobile still working nicely. All parameters were fine. Only SIMs were out of order due to water ingress in the SIM slot. I dried it up with a air blower, inserted the SIM and they started working fine. There was no water ingress to any other parts of the mobile. The net connectivity was working fine.This was a pleasant surprise to me. I have decided to buy only One plus for any future purchase. I highly recommend this.Thank you One Plus. Have been using for a couple of months and so far so good.Performance is good, camera quality is very good. Battery lasts for more than 1.5 days easily. Not a gamer, so can't judge on graphics. Camera Quality is very nice. And Sound. It's good. Has all features that I can use.Every thing is good, like battery backup,& Display is good. It does it work very well. It's review after 1.5 year. Overall good but camera quality not too good working good, no heating,no hanging, I had purchased this phone on sept 2023 at 19,999k but now I can see a huge price drop the product, however the the phone is actually a choice and battery is also good no heat issue performs well. Only """
    # print(SummarizeProduct(st))
    re = SummarizeProduct(st)
    # print(st)
    # return jsonify({'pros': 'succ'})
    return jsonify({'pros': re['pros'],'cons':re['cons']})

@app.route('/chatbot',methods=['POST'])
def getChat():
    # ChatBot.start('')
    global ob
    query = request.json['prompt']
    link = request.json['product']
    isStart = request.json['isStart']
    if(isStart == True):
        ob.start(query)
        return jsonify({'message':'Sure, Provide me the query about the product'})
    else:
        res = ob.query(query).replace('*','\n')
        return jsonify({'message':res})

    # pass

@app.route('/analysis',methods=['POST'])
def analyser():
    # print(request.json)
    query = request.json['prompt']
    # print(query)
    response = Analysis(query)
    # return jsonify({query:query})
    return jsonify(response)

if __name__=='__main__':
    app.run(debug=False)