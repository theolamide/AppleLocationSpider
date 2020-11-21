import requests


# import re
# import csv

req_header = {
    'authority': 'rh.com',
    'method': 'GET',
    'path': '/static/js/12.f96d12c0.chunk.js',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'referer': 'https://rh.com/store-locations/stores',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = 'https://rh.com/store-locations/stores'

r = requests.get(url=url, headers=req_header)
rResponse = r.content

print(rResponse)
