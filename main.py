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

counter = 1

with open("quotes.txt","w") as quotes_file:
    while True:
        quote = soup.find('div',id='pos_1_' + str(counter))
        if quote == None:
            break

        counter += 1

        if quote.find('a',class_='oncl_q') == None:
            continue

        quote_text = quote.find_all('a',class_='oncl_q')
        quote_text = "".join(quote_text[len(quote_text) - 1].text.split("\n"))
        author = "".join(quote.find('a',class_='oncl_a').text.split("\n"))

        quotes_file.write("\"" + quote_text + "\"" + "\n")
        quotes_file.write("- " + author + "\n\n")