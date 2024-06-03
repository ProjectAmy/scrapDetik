import requests

# json_data = requests.get('https://www.floatrates.com/daily/idr.json')
json_data = {"aud": {"code": "AUD", "alphaCode": "AUD", "numericCode": "036", "name": "Australian Dollar",
                     "rate": 9.272137227631e-5, "date": "Mon, 3 Jun 2024 06:55:02 GMT", "inverseRate": 10785},
             "cad": {"code": "CAD", "alphaCode": "CAD", "numericCode": "124", "name": "Canadian Dollar",
                     "rate": 8.4033379694019e-5, "date": "Mon, 3 Jun 2024 06:55:02 GMT",
                     "inverseRate": 11900.033101622},
             "cny": {"code": "CNY", "alphaCode": "CNY", "numericCode": "156", "name": "Chinese Yuan",
                     "rate": 0.00044651831247102, "date": "Mon, 3 Jun 2024 06:55:02 GMT",
                     "inverseRate": 2239.5498058434},
             "eur": {"code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro",
                     "rate": 5.6782568382012e-5, "date": "Mon, 3 Jun 2024 06:55:02 GMT",
                     "inverseRate": 17611.038536904}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['rate'])
    print(data['date'])
    print('\n')
