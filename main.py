from bs4 import BeautifulSoup
import requests


TOPIC = input() + "-quotes" 
URL = "https://brainyquote.com/topics/" + TOPIC

request = requests.get(URL)

if request.status_code == 404:
    print("Topic not found")
    exit()

page = request.text

soup = BeautifulSoup(page,'html.parser')