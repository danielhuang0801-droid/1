
import requests
from bs4 import BeautifulSoup
import time


stock = ["1101", "2330", "1102"]

for i in range(len(stock)): 
    stockid = stock[i]
    
    # 
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"
    
    #
    r = requests.get(url)
    
    # 
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #
    price = soup.find('span', class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"]).getText()
    
    #
    message = "股票 " + stockid + " 即時股價為 " + price
    
    #
    token =  8711541708: AAHm7bLc83S8ABZh3vRE8
     -3 qCvx0Kv&GUSg # 替換成 BotFather 給的 Token
    chat_id = 6275017364  # 替換成 userinfobot 給的 ID
    
  
    api_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(api_url)
    
    
    time.sleep(3)
