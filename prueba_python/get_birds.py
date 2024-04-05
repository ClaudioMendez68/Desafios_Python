import requests, json

def get_request(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__':    
    response = get_request("https://aves.ninjas.cl/api/birds")
    print(response)