from helper import read_csv
from helper import read_webhook
from helper import send_webhook
import httpx
import json
import time



class Tracker:

    def __init__(self,address,name,webhook_url,api_key) -> None:
        self.api_key = '34WBZMUXKFIXA18274DXHJASFH1B7J4GTK'
        self.address = read_csv([1])
        self.name = read_csv([2])
        self.webhook = read_webhook('webhook.txt')

    def fetch_transactions(self):
        #send request to arbiscan api
        
        req = httpx.get('https://api.arbiscan.io/api?module=account&action=tokentx&address={}&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey={}'.format(self.address,self.api_key)).json()['result']
        
        fetch_ts = (req['timeStamp'])
        fetch_hash = (req['hash'])
        add_from = (req['from'])
        add_to = (req['to'])
        contract_add = (req['contractAddress'])
        value = (req['value'])
        symbol = (req['symbol'])
            

        send_webhook(fetch_ts, fetch_hash, add_from, add_to,contract_add,value,symbol)




