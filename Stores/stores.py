import requests
import re

r = requests.get('https://www.apple.com/retail/storelist/')
rResponse = r.text.encode("utf-8")

toLook = re.findall(r'https://www.apple.com/retail/\w+', rResponse)
for look in toLook:
    print(look)
