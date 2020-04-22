import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.it/Acer-Predator-PT515-51-72QK-Notebook-Processore/dp/B07PPP9R89/ref=sr_1_fkmr1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=predator+helios+500&qid=1568128819&s=gateway&sr=8-1-fkmr1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()
    converted_price = float(price[0:5])

    print(title.strip())

    if converted_price < 3000:
        send_mail()
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('thang.luongcao@gmail.com', 'xfwqeqwaztdscmdg')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.it/Acer-Predator-PT515-51-72QK-Notebook-Processore/dp/B07PPP9R89/ref=sr_1_fkmr1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=predator+helios+500&qid=1568128819&s=gateway&sr=8-1-fkmr1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'thang.luongcao@gmail.com',
        'thang.luongcao@gmail.com',
        msg
    )
    print('HEY, EMAIL HAS BEEN SENT!')

    server.quit

while True:
    check_price()
    time.sleep(60*60)
