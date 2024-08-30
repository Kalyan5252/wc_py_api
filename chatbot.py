from dotenv import load_dotenv
import re
import google.generativeai as genai
load_dotenv()


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
    
    
class ChatBot:
    def start(self,link):
        self.app = GeminiTerminalApp()
        self.app.run(f'clarify my doubts about this product : {link}')
    
    def query(self,q):
        return self.app.run(f'{q}. keep answer breif and understandable')

# def chat
# o = ChatBot()
# o.start('https://www.amazon.in/CAPPL-Stunning-Spathyphyllum-Included-Fertilizer/dp/B075N8FXJ8/ref=sr_1_4?_encoding=UTF8&content-id=amzn1.sym.93cbdfa7-dde3-4a76-b5ca-e61e354a5ed2&crid=2EHC2GOPHE9F8&dib=eyJ2IjoiMSJ9.jrBZAuxLc5l_imge1jit1xY2HaYXHjIHCx_BSejBKm-4OVEwZBwixMEMPAfjq5NHdslp39uRHJPvIBKEQvHAh7Ygxj3jMkW2N4YX5zjLxE6UpCCzjIZ3geJZrofdjk4c0J-jSllUm08CltVdh6NmTmZfNzrX_8gbZtV56bcoHlf4HyRKrmDROD9hzuXVC17EXIvhUk7pV6kqPSeY9Ldl6D8CanLNZvVDkpZTmGUk9DZqEkQVyW0kn7V4xjDzz5KPUGlEDV1q3NClUcuK8Ix50K7EPOBnw0Df75IVz3ni-P8.UU1XX0zEe3lq5IEmrT0G-Emt4HQcVBEgwNetiUJdAyk&dib_tag=se&keywords=indoor+plants+for+living+room&pd_rd_r=19edc158-6237-4a9e-bdda-248b5f00f998&pd_rd_w=j4nZ5&pd_rd_wg=x6iY2&pf_rd_p=93cbdfa7-dde3-4a76-b5ca-e61e354a5ed2&pf_rd_r=M3QS8K6AF5TEKJ5QXED6&qid=1725021442&refinements=p_n_deal_type%3A26921224031%2Cp_n_pct-off-with-tax%3A2665401031&rnid=2665398031&s=garden&sprefix=indoor+plants+for+%2Caps%2C318&sr=1-4')
# print(o.query('what is it?'))
