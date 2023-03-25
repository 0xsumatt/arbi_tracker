# arbi_tracker

You should be able to install from requirements but incase it doesn't work you need httpx,dotenv,rich and discord_webhook to make this work.

First thing you'll need is an arbiscan api key, you can get one here by creating an account https://arbiscan.io/register

you then need to create a .env file and use the key API_KEY = "YOUR KEY HERE"
from here you then need to add your discord webhook to the webhook.txt file and enter addresses into the csv file alongside a name you want associated with the address (can be anything)
From here it's simply a matter of running main.py and selecting menu option 1.

This is highly experimental and hasn't really been tested much so please don't rely too heavily on it

*TODO
-Add async or threading
-Tidy up the code more
