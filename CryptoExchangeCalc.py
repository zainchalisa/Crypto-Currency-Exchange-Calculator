from requests import Request, Session
import json
import pprint


#BTC current price
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'slug': 'bitcoin', 'convert': 'USD'}

headers = {'Accepts':'applications/json', 'X-CMC_PRO_API_KEY':'add personal key'}

session = Session()
session.headers.update(headers)

response= session.get(url, params=parameters)
bitCoinprice =json.loads(response.text)['data']['1']['quote']['USD']['price']

#ETH current price
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'slug': 'ethereum', 'convert': 'USD'}

headers = {'Accepts':'applications/json', 'X-CMC_PRO_API_KEY':'add personal key'}

session = Session()
session.headers.update(headers)

response= session.get(url, params=parameters)

ethereumPrice= json.loads(response.text)['data']['1027']['quote']['USD']['price']

#Litecoin current price
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'slug': 'litecoin', 'convert': 'USD'}

headers = {'Accepts':'applications/json', 'X-CMC_PRO_API_KEY':'add personal key'}

session = Session()
session.headers.update(headers)

response= session.get(url, params=parameters)

litecoinPrice= json.loads(response.text)['data']['2']['quote']['USD']['price']

#Cardano current price
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'slug': 'cardano', 'convert': 'USD'}

headers = {'Accepts':'applications/json', 'X-CMC_PRO_API_KEY':'add personal key'}

session = Session()
session.headers.update(headers)

response= session.get(url, params=parameters)

cardanoPrice= json.loads(response.text)['data']['2010']['quote']['USD']['price']

#DOGE current price
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'slug': 'dogecoin', 'convert': 'USD'}

headers = {'Accepts':'applications/json', 'X-CMC_PRO_API_KEY':'add personal key'}

session = Session()
session.headers.update(headers)

response= session.get(url, params=parameters)
        
dogecoinPrice= json.loads(response.text)['data']['74']['quote']['USD']['price']


print('Welcome to the Crypto Currency Exchange Calculator')

print()

print('How may we help you today?')

print()

options=['1. Find the current value of a Crypto Currency', '2. Exchange USD for Crypto', '3. Exchange Crypto for USD']
for i in options:
    print(i)

print()

selection = int(input("What is your selection: "))

print()

if selection == 1:

    cryptos = ["1. Bitcoin", "2. Ethereum", "3. Litecoin", "4. Cardano", "5. Dogecoin"]
    print()
    print("What current Crypto Currency price are you looking for?")
    for i in cryptos:
        print(i)

    convert= str(input("Enter the Crypto Currency you are trying to find the price of: "))

    print()

    if convert == 'Bitcoin':
        print('Current price of Bitcoin is: $' ,bitCoinprice)

    if convert == 'Ethereum':
        print('Current price of Ethereum is: $' ,ethereumPrice)

    if convert == 'Litecoin':
        print('Current price of Litecoin is: $' ,litecoinPrice)   

    if convert == 'Cardano':
        print('Current price of Cardano is: $' ,cardanoPrice)
    
    if convert == 'Dogecoin':
        print('Current price of Dogecoin is: $' ,dogecoinPrice)

if selection == 2:

    print('How much are you looking to invest?')
    print()
    cash= float(input('Enter USD amount here: $'))
    print()
    print('Thank you for that information!')
    print()
    cryptos = ["1. Bitcoin", "2. Ethereum", "3. Litecoin", "4. Cardano", "5. Dogecoin"]
    print("What Crypto Currency are you looking to convert your USD to?")
    for i in cryptos:
        print(i)

    convert= str(input("Enter the Crypto Currency you are trying to convert to: "))

    if convert == 'Bitcoin':
        usd = cash / bitCoinprice
        print('The amount of Bitcoin you will recieve is: ', usd) 

    if convert == 'Ethereum':
        usd = cash / ethereumPrice
        print('The amount of Ethereum you will recieve is: ', usd) 

    if convert == 'Litecoin':
        usd = cash / litecoinPrice
        print('The amount of Litecoin you will recieve is: ', usd) 
    
    if convert == 'Cardano':
        usd = cash / cardanoPrice
        print('The amount of Cardano you will recieve is: ', usd) 
    
    if convert == 'Dogecoin':
        usd = cash / dogecoinPrice
        print('The amount of Dogecoin you will recieve is: ', usd) 
        
if selection == 3:

    print('The Crypto Currencies currently available are:')
    cryptos = ["1. Bitcoin", "2. Ethereum", "3. Litecoin", "4. Cardano", "5. Dogecoin"]
    print()
    print("What Crypto Currency do you currently have?")
    for i in cryptos:
        print(i)

    print()

    convert= str(input("Enter the Crypto Currency you are trying to convert to USD: "))

    print()

    print('Thank you for that information!')

    print()

    if convert == 'Bitcoin':
        print('How much Bitcoin are you looking to convert to USD?')
        crypto = float(input('Enter the amount here: '))
        usd = crypto * bitCoinprice
        print()
        print('The amount of USD you will recieve is: $', usd) 

    if convert == 'Ethereum':
        print('How much Ethereum are you looking to convert to USD?')
        crypto = float(input('Enter the amount here: '))
        usd = crypto * ethereumPrice
        print()
        print('The amount of USD you will recieve is: $', usd) 
        

    if convert == 'Litecoin':
        print('How much Litecoin are you looking to convert to USD?')
        crypto = float(input('Enter the amount here: '))
        usd = crypto * litecoinPrice
        print()
        print('The amount of USD you will recieve is: $', usd) 
        
    
    if convert == 'Cardano':
        print('How much Cardano are you looking to convert to USD?')
        crypto = float(input('Enter the amount here: '))
        usd = crypto * cardanoPrice
        print()
        print('The amount of USD you will recieve is: $', usd) 
    
    if convert == 'Dogecoin':
        print('How much Dogecoin are you looking to convert to USD?')
        crypto = float(input('Enter the amount here: '))
        usd = crypto * dogecoinPrice
        print()
        print('The amount of USD you will recieve is: $', usd) 