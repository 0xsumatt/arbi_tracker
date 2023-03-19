import csv
from discord_webhook import DiscordWebhook, DiscordEmbed

def read_csv(filename:str):
    with open(filename,'r') as csvFile:
        read_file = csv.DictReader(csvFile)
        return read_file

def read_webhook(webhook:str):
    with open(webhook,'r')as webhook:
        webhook_url = webhook.readline()
        return webhook_url

def send_webhook(fetch_ts:int, fetch_hash:str, add_from :str, add_to:str,contract_add:str,value:float,symbol:str):
    hook = DiscordWebhook(read_webhook('webhook.txt'))
    embed = DiscordEmbed(title = "New Transaction", url ='https://arbiscan.io/tx/{}'.format(fetch_hash))
    embed.add_field('Timestamp', value = fetch_ts)
    embed.add_field(name = "From Address", value = add_from)
    embed.add_field(name = "To Address", value = add_to)
    embed.add_field(name = "Contract", value = contract_add)
    embed.add_field(name = "Symbol", value = symbol)
    embed.add_field(name = "Value", value = value)