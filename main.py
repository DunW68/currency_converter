import requests
import json


def convert():
    global js
    global cache
    another = input('What currency do you want? > ')
    while len(another) != 0:
        amount = float(input('How much do you have? > '))
        if cache.get(another) is None:
            print('Checking the cache...')
            print('Oh! It is in the cache!')
            print(f'You received {round(amount * cache[another], 2)} {another.upper()}.')
        else:
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            cache[another] = js[another]['rate']
            print(f'You received {round(amount * cache[another], 2)} {another.upper()}.')
        another = input('Maybe you want to convert in another one? (Press Enter if not) > )')


cache = dict()
current = input('What currency do you have? > ')
js = json.loads(requests.get(f'http://www.floatrates.com/daily/{current}.json').text)
if current == 'usd':
    cache['usd'] = 1
    cache['eur'] = js['eur']['rate']
elif current == 'eur':
    cache['usd'] = js['usd']['rate']
    cache['eur'] = 1
else:
    cache['usd'] = js['usd']['rate']
    cache['eur'] = js['eur']['rate']
convert()
