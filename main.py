import requests
from bs4 import BeautifulSoup
import time
import schedule
from flask import Flask, request, jsonify, session
# from flask_bcrypt import Bcrypt #pip install Flask-Bcrypt = https://pypi.org/project/Flask-Bcrypt/
# from flask_cors import CORS, cross_origin #ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors
# from models import db, User
 
app = Flask(__name__)
banks_hose = ['ACB', 'BID', 'CTG','EIB', 'HDB', 'MBB', 'MSB','OCB','SHB','SSB','STB','TCB','TPB','VCB','VIB','VPB']
banks_hnx = ['NVB', 'BAB']
data = {}
def get_data_from_web(bank):
    print('bank', bank)
    url = f'https://simplize.vn/co-phieu/{bank}/lich-su-gia'
    response = requests.get(url)
    data = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tbody = soup.find('tbody', class_='simplize-table-tbody')
        if tbody:
            tr_simplize_table_row = tbody.find_all('tr', class_='simplize-table-row')
            h6_css_cvilom_today = tr_simplize_table_row[0].find_all('h6', class_='css-cvilom')
            h6_css_cvilom_yesterday = tr_simplize_table_row[1].find_all('h6', class_='css-cvilom')
            stockHistory = {}
            today = h6_css_cvilom_today[0].text.strip()
            stockHistory['open'] = h6_css_cvilom_today[1].text.strip()
            stockHistory['high'] = h6_css_cvilom_today[2].text.strip()
            stockHistory['low'] = h6_css_cvilom_today[3].text.strip()
            stockHistory['close_yesterday'] = h6_css_cvilom_yesterday[4].text.strip()
            stockHistory['volume_yesterday'] = h6_css_cvilom_yesterday[5].text.strip()
            data[today] = stockHistory
    return data
@app.route("/")
def hello_world():
    return "Hello, World!"
def crawl(banks_hose,banks_hnx):
    for  bank in banks_hose:
        data[bank] = {}
        data[bank] = get_data_from_web(bank)
    for bank in banks_hnx:
        data[bank] = {}
        data[bank] = get_data_from_web(bank)
    print(data)
    return data

schedule.every(1).minutes.do(crawl, banks_hose=banks_hose,banks_hnx=banks_hnx)
while True:
    schedule.run_pending()
    time.sleep(1)