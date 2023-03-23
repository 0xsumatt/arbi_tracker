
from helper import read_webhook,send_webhook,get_latest_block
from logger import logging
import httpx
import json
import time

logger= logging()

class Tracker:

    def __init__(self,address,name,api_key) -> None:
        self.api_key = api_key
        self.address = address
        self.name = name
        self.webhook = read_webhook('webhook.txt')
        

    def fetch_transactions(self):
        latest_block = get_latest_block()
        start_block = latest_block - 10
        #send request to arbiscan api
        
        req = httpx.get('https://api.arbiscan.io/api?module=account&action=tokentx&address={}&page=1&offset=1&startblock={}&endblock=99999999&sort=desc&apikey={}'.format(self.address,start_block,self.api_key)).json()
        if req['message'] == 'OK':
            logging.success("Address valid")
            try:
                from_addresss = (req['result'][0]['from'])
        
                to_address = (req['result'][0]['to'])
                fetch_ts = (req['result'][0]['timeStamp'])
                fetch_hash = (req['result'][0]['hash'])
                contract_add = (req['result'][0]['contractAddress'])
                symbol = (req['result'][0]['tokenSymbol'])
                value = (req['result'][0]['value'])
                logging.success("new Transaction found for wallet named :", self.name)
                send_webhook(fetch_ts,from_addresss,self.name,fetch_hash,to_address,contract_add,value,symbol)
        
            except Exception as e:
                logging.warning("No new transactions logged")
                pass


        if req['message'] == 'No transactions found':
            logging.warning("No transactions found")

        else:
            logging.error("invalid address")
            
            pass
        

        




