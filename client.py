import requests


# ____________________POST_________________________

data = requests.post('http://127.0.0.1:5000/ads/',
                     json={'title': 'Strawberry', 'description': 'Red strawberry', 'owner': 'Name_2'})
print(data.status_code)
print(data.text)

data = requests.post('http://127.0.0.1:5000/ads/',
                     json={'title': 'Banana', 'description': 'Yellow Banana', 'owner': 'Name_1'})
print(data.status_code)
print(data.text)

data = requests.post('http://127.0.0.1:5000/ads/',
                     json={'title': 'Ключ', 'description': 'Ключ от квартиры, где деньги лежат', 'owner': 'Лопух'})
print(data.status_code)
print(data.text)


# _____________________GET_________________________

# data = requests.get('http://127.0.0.1:5000/ads/1/')
# print(data.status_code)
# print(data.json())

# data = requests.get('http://127.0.0.1:5000/ads/2/')
# print(data.status_code)
# print(data.json())
#
# data = requests.get('http://127.0.0.1:5000/ads/3/')
# print(data.status_code)
# print(data.json())


# ____________________Patch________________________

# data = requests.patch('http://127.0.0.1:5000/ads/1', json={'owner': 'Patch'})
# print(data.status_code)
# print(data.text)


# ___________________DELETE________________________

# data = requests.delete('http://127.0.0.1:5000/ads/1/')
# print(data.status_code)
# print(data.json())

