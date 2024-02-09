import requests

def get_ip():
    response = requests.get('https://api.ipify.org/?format=json').json()
    print(response)
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipinfo.io/161.185.160.93/geo').json()
    location_data = {
       
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "loc": response.get("location"),
        "org":response.get(""),
         "postal":response.get(""),
         "timezone":response.get(""),
         "readme":response.get("")
    }
    return location_data


print(get_location())