from dotenv import load_dotenv
import re
load_dotenv()

import google.generativeai as genai

class GeminiTerminalApp:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])
        genai.configure(api_key="AIzaSyCYDGQXaq8b69eR4LJtj0Es7jJAqFGf0GI")
    def remove_emoji(self,text):
  # Define the emoji pattern with raw strings for proper unicode support
      emoji_pattern = re.compile(r"""
        \U0001F600-\U0001F64F  # emoticons
        |\U0001F300-\U0001F5FF  # symbols & pictographs
        |\U0001F680-\U0001F6FF  # emoticons (supplemental)
        |\U0001F1E0-\U0001F1FF  # flags (supplemental)
        |\U00002702-\U000027B0  # dingbats
        |\U000024C2-\U00001F251  # additional emoticons
        """, flags=re.UNICODE)
      return emoji_pattern.sub('', text)
    
    def get_gemini_response(self, question):
        response = self.chat.send_message(question, stream=True)
        return response

    def run(self,user_input):
        response = self.get_gemini_response(user_input)
        res = ''
        for chunk in response:
            res += (chunk.text)
        return res


app = GeminiTerminalApp()
def process(data):
    data=app.remove_emoji(data)
    data = app.run("Summarize this into 5 pros and 5 cons"+data)
    return data

def product_comp(product1,product2):
    flag = app.run(f"I need your help to identify whether two products are identical or not.These are the descriptions of the products \n 1. {product1}\n2.{product2} \n Just return me the boolean value whether these products are identical or not. no explanation only True or False")
    return flag

if __name__== '__main__':
    data = process('''The iPhone 15 Pro Max is a powerhouse device, offering top-tier performance, an exceptional camera setup, and a gorgeous display. Its sleek design and long battery life ensure it's ready for anything. While it's pricey, the overall experience justifies the investment for tech enthusiasts and professionals alike. The iPhone 15 Pro Max is a very versatile phone with professional cameras having 4 options of optical lenses of 0.5x, 1x, 2x and 5x and a macro lens option. It is better and more cost effective than having an SLR camera with many lens options, which you need to acquire. The charge lasts long enough for my filming videos of YouTube channel. Superb Nice No regrets. It is as if I bought from a showroom only which got delivered at home. Recently, I updated to the latest version of 17.5.1 added emojis something like that and after that my device touch screen isn't responding now. And when I used the phone earlier, the device gets too warm easily when I started to play games...and I contacted the Amazon and iOS support and told me to visit the service centre and the service centre is like 1-2 days far from my home location. This isn't something I expected. The phone is very expensive and I bought recently, just in 1-2 months the device isn't usable, it need to be trash now smh...The device isn't even charging now.. Excellent device at any expects. I recently upgraded to the Apple 15 Pro Max, and while the enhanced camera is undoubtedly impressive, but I feel that it falls short of delivering a truly groundbreaking experience. If you're already using the 13 pro or 14 Pro, there seems to be little incentive to make the leap.

The camera improvements are noteworthy, capturing detail and clarity like never before. However, beyond this feature, the 15 Pro Max doesn't offer a significant leap in terms of innovation. Personally, I find the Pro versions more manageable in hand, and the Max variant, although boasting a larger screen, can be a bit unwieldy.

In essence, the 15 Pro Max is a solid device with a stellar camera, but for those already enjoying the perks of the previous Pro models, the upgrade might not feel as compelling. Ok Heating Issue during Charging & Required AC room for Charging otherwise charging will stop due to mobile heating / high temperature which is a major issue in Apple iPhone 15 Pro Max.

I suggest avoiding it, especially in the summer, if you don't have an AC room.

This is my personal experience!! The battery is little problem need to charge once in a day. But other then that all good picture quality is epic attached moon pic for example Good Product but Price Was High and I Trust amazon Thank you Just amazing product. Actually I like to purchase online products but as it's so expensive, I tried to purchase from local store in Barasat but they told me 8 thousand more than online price (Only phone's price)😀 even without charger, screen protector and back cover.

I got it on online with everything only ₹1,52,000. Although it was a little difficult to buy, as you know it is not easy to transfer the higher amounts within short time. 😀

However, Thanks to Amazon team and specially thanks to my IDOL "Steve Jobs" 🙏🤗 I think there is no need to justify that this is the best phone on the planet. In every aspect this is best. Camera setting not available, so photos not better than Samsung m34, likely Caller tune should not set, call record not available. Should not connect to laptop. Download space not available Packing is bad. There's a tampered package within a new package. The tampered package contained the phone. But the phone is looking good As I was aware that what I need and what I was paying for, I needed a quality mobile with best hardware and software combination.
I need the OS to be clean without any bloatware which I got.
I don't play games. For moderate use of Social media, whatsapp, youtube, audible (audio books), music while exercising, Battery life is around 2 days or sometimes more than 2 days. If you are a gamer or use mobile a lot you might need to charge your mobile everyday.
Camera is good. So far the pictures I took the quality is good.
Not explore the processor's capacity yet but Never hanged or never will for me (not a heavy user so won't be a problem). A phone that screams that you are doing very well for yourself. Don’t get me wrong, it works extremely well and I am completely satisfied with it. but, it is way too expensive for a phone. I have a pixel 8 which as a secondary phone which costs way less and I am satisfied with that as well. Nevertheless, nothing can replace an iPhone for me due to personal preferences I would prefer this over S24 ultra. Used both phones and impressed by this phone. Yes I agree s24 ultra had few more features but in terms of quality 15 pro max wins. And camera quality is far better than s24ultra. But it differs on a customer’s choice. Mind blowing Speed. No heating issues. Awesome camera for videos and photography (astro). The phone is really good it had some overheating issue as heard but not faced any it was due to software update now it is all fixed I still did not had any issue regarding overheating. The phone is really fast and the battery life is awesome. The new action button is really handy and useful. The camera is the best camera an iPhone ever had the photos are stunning and spectacular…. I am satisfied with the phone.. Play Video
Phone is just amazing and It’s a fantastic phone…the feel and comfort in hand is awesome…looks stunning…also the brand appeal of Apple is fabulous. Camera is the best, performance is over the top…really fast and the games you can play are of play station’s…can any other phone do that…also the video quality is very nice… Wow, such a great phone, superfast, great performance, great cameras great looks I’m in love with my black titanium so strong so light so pro I recently switched from android to iphone. So i am liking the good audio quality, camera and everything. "I spent 152,000 rupees on an iPhone 15 Pro Max, but it doesn't seem worth more than a 10,000 rupee phone. I've encountered software issues, with many apps and games not performing well. There are problems with phone calls—calls drop frequently, requiring me to restart the phone each time. Initially, I thought it might be due to other apps or network providers, but I used to use an Android phone with the same network and common apps, and they performed much better. This iPhone keeps crashing apps and games, which, in my opinion, makes it not worth the price."  Ultimate performance but some bug issue in 17.2.1 update and FB is not functioning properly….😏😏😏😏😏Lot of BUG issues are experienced in this phone and needs to correct it. Fake product , paid 1,89,400/-
got 0 refund It’s a great buy. I upgraded from XS Max and am so glad I decided to get this. It’s pricey but worth it. Very powerful battery too It’s around 2months I have been using this device and it has been working flawlessly. No heating issues or such. Totally worth the upgrade because of the camera. We have received the iPhone 15 Pro Max, natural titanium color, and 256 GB storage capacity. The phone is good-looking and fast. It gets charged with the Apple 20W USB-C Power Adapter (purchased separately). It also charges well using my 3-year-old Mi wireless charger (Qi charging). Overall, we are happy with the iPhone. Phone battery down very fast  Good This is my 1 st pro iPhone. And so far I’m really impressed with the performance and simplicity of the product. I have purchased natural titanium and it's really awesome. My first phone purchased with my hardwork. Didn't sold my kidney for it 😂😂  No heating issue till now running well with the new software update I have installed lots of apps and the ph is running well Lightning fast,titanium tantrums Really disappointing to see that being a premium phone it’s heating issue is just in another level Superb Fast charging  I only use i phone pro maxs and when new model come i gift my old one to my subscriber please apple make i phone 16luli max lulliniam  My biggest mistake buying this, you can to same things in 15 and 14 and 13 iphone 15pro max ios worst pro max I purchased. I already have 13 and 14 pro max, Time to switch to Samsung. The screeenshot you see shows 85% baterrey charge but it has been only 5 min after i made a full charge of the phone Good mobile but Too much price. Features are ok but price are extra ordinary. Not value for money. Avoid if you have not enough money All good... Not a compare anything 😍
Rate 💯 to 💯 😍
Recommend to everyone perches 😍😍😍 Nice 💯😍😍 Thanks Best IPhone Ever And I Loved This Phone so much 😍😍😘😘.
Pros - Best Battery Life , Value for Money Phone, Very Smooth Display ever, very Smooth in Touch, Best Camera ever.
I changed my phone from IPhone 12 to IPhone 15 Pro Max .
I Loved This Phone Battery life is quite bad , honestly the battery life should be a bit better I this range of price. The box had a different colour. I order black Titanium....box was black Titanium but phone was natural titanium inside ...It's heart wrenching...Trust shaken...

The phone looks used

It can happen with Apple product also...it's a shock. Play Video
Didn't use a screen guard for a week and found a scratch on the screen. What a stupid phone. 160k phone and you will get a scratch without even holding the phone. Better get a screen guard the day you receive the phone. It is good for gaming and personal usage and it is more better than 14 series, the camera clarity is super. this is very bad iphone it lacks kanye west it is travis scott and has a jawline it is very ewwwwwwwww we cannot play cricket wws💀💀💀💀 Got a defective product where the camera doest load The haptic music on the iPhone 15 Pro Max is amazing—it almost feels like a mini massager in my hand! 😂 box damaged, no new device smell. Completely ruined my unboxing experience. But the phone is amazing.  Don't think about it if you want to go for a flagship just go for it. It's an overall package,but the battery life is at another level it goes on for 2 days Bhaiya theek thakh laga do har baar apse hi se lete hain. (Reviewing that I Might delete later) Thank you so lagg cant even play hill climb racing smoothly . dont waste money . nokia is better buy nokia 11 pro max that can run everything smoothly Great phone with perfect camera quality , battery life is 100 no over heating charging 8s decent.
Best in stability.
Brightness is good.
Certainly awesome Nothing to dislike battery life is too good
Love the look
Best camera feture
This worth the money no regret ✌
Just go & buy it & try it . The iPhone 15 Pro Max is a powerful and feature-packed device with a stunning display and excellent camera capabilities. However, the high price point may deter some potential buyers.  Best camera till date and batter last for 1day and it feels very premium when you hold it and due to curve edge it doesn’t irritate If at all looking for pro model just because of lidar and action button and camera. Its not value for money as the charging and performance are not upto the mark for both pro and non pro models. I purchased iPhone 15 pro 128gb not happy Best Smartphone Ever
Camera 10/10
Processor 10/10
Videography 10/10
Display 10/10
Speakers 11/10
Type C 10/10
Battery Backup 11/10
Ecosystem 10/10 Heats very much during charger. Even if apple type c charger is used.
No much difference from 14 pro max. Play Video
We got scammed!! This is not an iPhone. Me and my husband are long time iPhone users and this is some cheap Android interface inside an iPhone casing. This seller doesn’t want to return our product or refund as “it is out of stock”. I am very very upset as this is a high value item that is completely useless. Slow, pixelated, not even iPhone interface. Beware!! After uprade display isnt working well after 2hrs of upgrades the display shutdown and later i had to take the mobile in service center they told me the display is gone. Waste of money If you already have 14 Pro or Pro Max then don't upgrade, but if you've any other Pro or non Pro models go for it. If you need an iPhone with 24-26hr battery life on a single charge then go for Pro Max models. No doubt Apple's 4K 60fps ProRes is really awesome, and the all new type-c port is the best thing Apple has done in years. Also all the type-c cables included in the box are woven design, now expecting this will not turn grey after few months of use. This Phone is like the Central processing unit (CPU) with a screen. It is fast as thunder and got heated like lava after using it for sometime. Camera is better than reflection of mirror and it's screen and overall body is weaker than a mirror i.e. it breaks easily. Do not buy ... I throwed it from my terrace and the phone got broken ... Bad quality..
Waste of money I don't like this product I think nothing has changed from iPhone 14 don't buy this phone or you well waste your 1,50,000 We Know Nowadays There was so much hate spreading on Iphone 15 Series But as i am a techie, i know most of the critics had never used and talking like trash bin. i Using From Past 1 month, If You Love Photography Or Pro-Gaming then you are good to take this smartphone. Just Dont Care The Criticism.
I Too Had Feel The Phone Is warm while heavy gaming and Photography, But was never like what had they said in news. I Loved The Photos The Phone Gives. A17 Pro , 3Nm ,Ray tracing , 5x zoom nailed it completely. A truly freaking flagship mobile so far. iOs 18 will make it more powerful. Overpriced. It should not cost more than 1.1L. Bought it at 1.6L viz 50K extra I felt. Go for 15 instead of pro max. Overhyped phone this one is 15 pro max >>>> all androids . the speed the camera the new ios justtt superb
the resident evil village runs so smoothly Iphone always the better than Android , I need the iphone please give me one Amazon please amazon Amazon Amazon When you hold this phone in your hand then only you can realise feeling of holding a premium phone 🍎 No heating issue. Even if they exists for you. Use phone on battery saver mode amazing performance Very good phone. Hate it ssoooooo much it’s 🤢🤢🤢it’s so disgusting it’s made with plastic and it’s fake full paid I lakh and a fault I took a refund Nice Phn bought under very good price Super sleek nice handy vulnerable best rate so budget in hatts of to apple for making value products iPhone battery and multimedia experience was very Poor Quality Don't buy this dumb iPhone 15 Pro Max 256 GB . Till this date it is the fastest iPhone for gaming and all over daily usage .
Strongest iPhone till now''').replace('\n\n','\n').split('\n')
    pros = data[1:6]
    cons = data[7:]
    pro = ''
    con = ''
    for i in pros:
        pro += i+'\n\n'
    for i in cons:
        con += i +'\n\n'
    print('PROS')
    print(pro)
    print('CONS')
    print(con)