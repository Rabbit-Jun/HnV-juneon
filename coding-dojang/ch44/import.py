import requests

r= requests.get('http://www.google.co.kr')
print(r.status_code)
