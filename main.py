import requests
import json
from babel import numbers
from bs4 import BeautifulSoup
import emoji
#_______________DOLLAR_________________
def dollars():
    rd = requests.get('https://www.navasan.net/last_currencies.php?csrf=c2x0MTFoYWg5M2h0YXNxNjljcDZkOTl0bTRlYmU4N2VkYTRhZjM2ZGRiMzUxZGQwMjM5MjE0MDExYTYxODFiY2U2aHR0cDovL3d3dy5uYXZhc2FuLm5ldC81NHRmJWY%3D&_=166019602')
    js = json.loads(rd.content)
    dollar = []
    dollprice = []
    for k,v in js['usd'].items():
        dollar.append(v)
    for g in dollar:
        dollprice.append(str(g))
    fs = f'قیمت دلار » {numbers.format_number(dollprice[0], "fa_IR") } تومان '
    return fs
dollarprice = dollars()
#_______________GOLD_________________
def gold():
    r = requests.get('https://www.navasan.net/gold_rates.php?csrf=ajA2bHF0aXA0ZTZvZjYzc243cTh0MXIzcHE1YjAzZmJlYmJkMDhmMDIwNTIxOGM0NzcyM2NkMjQ2ZjQ1YTVkYmQ2aHR0cDovL3d3dy5uYXZhc2FuLm5ldC81NHRmJWY%3D&_=166037333')
    js = json.loads(r.content)
    goldapp1 = []
    goprice = []
    for k,v in js['18ayar'].items():
        goldapp1.append(v)
    for d in goldapp1:
        goprice.append(str(d))     
    gss = f'قیمت طلای 18 عیار » {numbers.format_number(goprice[2], "fa_IR")} تومان'
    return gss
goldprice = gold()
#_______________bitcoin_________________
def bitcoin():
    r = requests.get('https://arzdigital.com/coins/bitcoin/')
    soup = BeautifulSoup(r.text , 'html.parser')
    for i in soup.select('#coin-details-page > section.arz-coin-page-body > div.arz-coin-page-data > div.arz-row-sb.arz-coin-page-data__gen-info > div:nth-child(2) > div.arz-row.arz-coin-page-data__info > div.arz-col-12.arz-col-sm-6 > div.arz-coin-page-data__coin-price-box > div:nth-child(2) > div.arz-coin-page-data__coin-price.coinPrice.btcprice.pulser'):
        return f'قیمت بیت کوین به دلار » {numbers.format_number(i.getText().replace("$","").replace(",",""), "fa_IR")} دلار'
bt = bitcoin()

#_______________SEND TELEGRAM_________________

em = emoji.emojize(':pushpin:', language='alias')

msg = f"""{em} {goldprice} 
 {em} {dollarprice}
 {em} {bt}
  """

token = 'توکن botfather رو اینجا قرار بدید'
chatid= 'chat id خودتون رو اینجا قرار بدید'


send = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + msg
response = requests.get(send)

print(response.json())
