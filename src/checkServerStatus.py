import requests

code = ''
while(code != 200 ):
    response = requests.get('http://localhost:4200')
    code = response.status_code
    print("not up")


