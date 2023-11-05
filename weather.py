
import requests

API_KEY = '760b703b3ef9fa0105b51247cc278cee'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = 'Ho Chi Minh'

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"


def get_response():
    return requests.get(url).json()
