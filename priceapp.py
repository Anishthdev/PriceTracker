import requests
from bs4 import BeautifulSoup
import smtplib
import time

a=input("ENTER PRODUCT URL")
URL=a
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price.replace(',','').strip('₹').strip(' '))
    converted_price = float(converted_price)
    if(converted_price < 21000.00):
        send_mail()
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('trackerprice92@gmail.com','bcjpcqzfskinealx')

    subject ='Price Drop Alert'
    body = 'Check the link : https://www.amazon.in/Fitbit-FB507BKBK-Smartwatch-Tracking-Included/dp/B07TWFVDWT/ref=lp_19136330031_1_1?srs=19136330031&ie=UTF8&qid=1571410965&sr=8-1'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'trackerprice92@gmail.com',
        'anamay22@outlook.com',
        msg
    )
    print('HEY! EMAIL HAS BEEN SENT')
    server.quit()

while(True):
    check_price()
    time.sleep(40)