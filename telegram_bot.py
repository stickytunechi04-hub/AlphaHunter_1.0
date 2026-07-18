import requests

from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data)

        if response.status_code == 200:
            return True
        else:
            print(f"❌ Telegram Error: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return False