import requests

response = requests.get("http://localhost:8080/https://www049.anzeat.pro/streamhls/91e22e411752c8b91e8cd2c1fb76241a/ep.1.1727973605.1080.m3u8",headers={"Origin":"x-requested-with"})
print(response.content)