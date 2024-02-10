import requests

#r=requests.get('https://ipinfo.io/161.185.160.93/geo')
#print(r.json())


def get_ip():
    response = requests.get('https://api.ipify.org/?format=json').json()
    print(response)
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipinfo.io/{ip_address}/geo').json()
    print(response)
     
print(get_location())
