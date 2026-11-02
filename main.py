import os
import requests

# 1. 從環境變數安全讀取金鑰
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# 2. Open-Meteo API 設定 (經緯度預設為台北市，可自行調整 latitude 與 longitude)
LAT = 25.0330
LON = 121.5654
WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=precipitation_probability_max&timezone=Asia%2FTaipei"

def main():
    # 取得天氣資料
    response = requests.get(WEATHER_URL)
    data = response.json()
    
    # 取得今天 (第一筆資料) 的最高降雨機率
    today_precip_prob = data['daily']['precipitation_probability_max'][0]
    print(f"今日最高降雨機率: {today_precip_prob}%")

    # 3. 判斷是否超過 60% (依照步驟2要求。若要配合標題70%，請改為 > 70)
    if today_precip_prob > 70:
        message = f"☔ 提醒：今天的最高降雨機率為 {today_precip_prob}%，記得帶傘喔！"
        send_telegram_message(message)
    else:
        print("降雨機率未達標，不發送通知。")

def send_telegram_message(msg):
    tg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(tg_url, json=payload)

if __name__ == "__main__":
    main()
