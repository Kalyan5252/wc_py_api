from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha
import pandas as pd

import re

from time import sleep,time


class Review_Price_Extract:
    
    def start(self):
        chrome_options = Options()
#         Uncommenting below 2 lines can disable the browser pop up
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument('--no-sandbox')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.check = WebDriverWait(self.driver,1)
        
        
    def you_ask_we_say(self,links,titles):
        d = dict(list(zip(titles,[0 for i in range(len(titles))])))
        
        for i in range(len(links)):
            d[titles[i]] = self.review_extract(links[i])
            print(i+1,' is done. sai is the reason. he extracted ',len(d[titles[i]]),' reviews')
        
        return d
        
    def bypass(self):
        try:
            self.link = self.driver.find_element(By.XPATH,"//div[@class = 'a-row a-text-center']//img").get_attribute('src')
            captcha = AmazonCaptcha.fromlink(self.link)
            captcha_v = AmazonCaptcha.solve(captcha)
            ip = self.driver.find_element(By.ID,'captchacharacters').send_keys(captcha_v)
            butt = self.driver.find_element(By.CLASS_NAME,"a-button-text")
            butt.click()
        except :
            return
        
    def amazon(self):
        self.driver.get(self.driver.find_element(By.XPATH,"//a[@class='a-link-emphasis a-text-bold']").get_attribute('href'))
        self.bypass()
        reviews = []
        def check():
            try:
                self.check.until(EC.presence_of_element_located((By.XPATH,"//li[@class='a-disabled a-last']")))
                return True
            except:
                return False
        
        while True:
            self.bypass()
            try:
                reviews.extend([i.text for i in self.driver.find_elements(By.XPATH,"//span[@data-hook='review-body']")])
                if check():
                    return pd.DataFrame({'Reviews':reviews})
                self.driver.find_element(By.XPATH,"//li[@class='a-last']").click()
            except:
                return pd.DataFrame(reviews)
            sleep(1)
            
    
    def flipkart(self):
        self.driver.get(self.driver.find_element(By.XPATH,"//div[@class='col pPAw9M']//a").get_attribute('href'))
        
        try:
            sleep(2)
            self.driver.get(self.driver.find_element(By.XPATH,"//div[@class='col-9-12']//a").get_attribute('href'))
        except:
            pass
        
        pn = int(self.driver.find_element(By.XPATH,"//div[@class='_1G0WLw mpIySA']//span").text.split()[-1])
        reviews = []
        link = self.driver.find_element(By.CLASS_NAME,'_9QVEpD').get_attribute('href')[:-1]

        for i in range(1,pn+1):
            reviews.extend(list(map(lambda i:i.text,self.driver.find_elements(By.XPATH,"//div[@class='ZmyHeo']"))))
            self.driver.get(link+str(i+1))
            
        return pd.DataFrame(reviews)
    
    def is_scrollbar_at_end(self):
        initial_scroll_position = self.driver.execute_script("return window.scrollY;")
        
        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
        sleep(2)    
        
        updated_scroll_position = self.driver.execute_script("return window.scrollY;")
        
        return initial_scroll_position == updated_scroll_position
    
    def myntra_extract(self,link):
        pid = self.driver.find_element(By.CLASS_NAME,'supplier-styleId').text
        self.driver.get('https://www.myntra.com/reviews/'+pid)

        while not self.is_scrollbar_at_end():
            pass
            
        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
        reviews = self.driver.find_elements(By.CLASS_NAME,'user-review-reviewTextWrapper')
        return pd.DataFrame(list(map(lambda i:i.text,reviews)))
            
    def review_extract(self,link):
        self.driver.get(link)
        if 'amazon' in link:
            return self.amazon()
        elif 'flipkart' in link:
            return self.flipkart()
        elif 'myntra' in link:
            return self.myntra_extract(link)
        else:
            return 'Error'
        
    def price_analysis(self,link):
        self.driver.get("https://pricehistoryapp.com/")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter name or paste the product link']").send_keys(link+Keys.ENTER)
        sleep(4)
        text = self.driver.find_element(By.XPATH,"//div[@class='content-width mx-auto px-3']").text
        for i in range(len(text)):
            if text[i:i+5] == '. Thi':
                text = text[i+1:]
                break
        
        price_pattern = re.compile(r'(\d+(\.\d+)?)')
        pcur, pmin, pavg, pmax = list(map(float,[match[0] for match in price_pattern.findall(text)]))
        
        if pavg > pcur:
            fairness = 50+(pavg-pcur)*50/(pavg-pmin)
        elif pavg < pcur:
            fairness = 50-(pcur-pavg)*50/(pmax-pavg)
        else:
            fairness = 50
            
        con = self.driver.find_element(By.XPATH,"//p[@class='text-gray-500 dark:text-gray-400 text-sm']").text
        url = self.driver.current_url.replace('/product/','/embed/')
        
        return {'fairness':fairness,'url':url,'context':con}
    def stop(self):
        self.driver.quit()
        
def search_and_extract_amazon(product_name):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    search_bar = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    search_bar.send_keys(product_name)

    search_bar.submit()

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(EC.title_contains("Amazon.in"))
    titles = []
    links = []
    sleep(5)
    pages = int(driver.find_element(By.XPATH,"//span[@class='s-pagination-item s-pagination-disabled']").text) - 1
    for i in range(pages):
      btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")))
      titles.extend(list(map(lambda x:x.text,driver.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//span[@class='a-size-medium a-color-base a-text-normal']"))))
      links.extend(list(map(lambda x:x.get_attribute('href'),driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"))))
      if len(titles) >= 50:
          break
      btn.click()
      WebDriverWait(driver, 15).until(EC.title_contains("Amazon.in"))
    
    driver.quit()
    return links, titles
        
if __name__ == '__main__':
    #links,titles = search_and_extract_amazon('AC')
    obj = Review_Price_Extract()
    obj.start()
    #print(obj.review_extract("https://www.flipkart.com/sony-alpha-full-frame-ilce-7m2k-bq-in5-mirrorless-camera-body-28-70-mm-lens/p/itm92df94dc68fff?pid=DLLF6QZPNKTQMS8J&fm=organic&ppt=dynamic&ppn=dynamic&ssid=fnewy5pmbk0000001706938474552"))
    #print(obj.review_extract("http://www.myntra.com/mailers/topwear/nobero/nobero-graphic-printed-drop-shoulder-sleeves-cotton-oversized-t-shirt/28699080/buy"))
    #print(obj.you_ask_we_say(links,titles))
    obj.stop()