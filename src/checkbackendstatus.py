import requests

code = ''
while(code != 200 ):
    try:
        response = requests.get('http://localhost:8090')
        code = response.status_code
    except:
        continue

    print("backend is running")

