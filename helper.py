
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from dotenv import load_dotenv
import os
import httpx
from logger import logging
logger = logging()

def read_api_key() -> str:
    #loading enviroment variables
    load_dotenv()
    Api_key = os.getenv('API_KEY')
    return Api_key



def read_webhook(webhook:str)-> str:
    with open(webhook,'r')as webhook:
        webhook_url = webhook.readline()
        return webhook_url

def send_webhook(fetch_ts:int,add_from:str,name:str, fetch_hash:str, add_to:str,contract_add:str,value:float,symbol:str):
    hook = DiscordWebhook(read_webhook('webhook.txt'))
    embed = DiscordEmbed(title = "New Transaction", url ='https://arbiscan.io/tx/{}'.format(fetch_hash))
    embed.add_embed_field(name = 'Timestamp', value = fetch_ts)
    embed.add_embed_field(name = "Wallet Name", value = name)
    embed.add_embed_field(name = "From Address", value = add_from)
    embed.add_embed_field(name = "To Address", value = add_to)
    embed.add_embed_field(name = "Contract", value = contract_add)
    embed.add_embed_field(name = "Symbol", value = symbol)
    embed.add_embed_field(name = "Value", value = value)
    hook.add_embed(embed)
    response = hook.execute()

def get_latest_block()->int:
    ts = int(time.time())  
    key = read_api_key()
    #sending request to arbiscan api to get latest block
    get_block = httpx.get("https://api.arbiscan.io/api?module=block&action=getblocknobytime&timestamp={}&closest=before&apikey={}".format(ts,key)).json()
    if get_block['result'] == "Inavlid API Key" or get_block['message'] == "NOTOK":
        logging.error("API Key is incorrect, please check again")
        exit()
    else:
        return int(get_block['result'])
        



