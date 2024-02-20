import argparse
parser = argparse.ArgumentParser(description='API Authentication')
parser.add_argument('-u','--username', help='RecNet Username', required=True)
parser.add_argument('-p','--password', help='RecNet Password', required=True)
args = vars(parser.parse_args())

print(parser.parse_args());

'Get username from argparse'
user = args["username"]
print(user)
'Get Password from argparse'
passwd = args["password"]
print(passwd)




import time
try:
    import requests
except:
    print('''You do not have the requests library installed, you need to install it via the following command:
        pip install requests
    Thank you!''')
try:
    import recnetlogin as rnl
except:
    print('''You do not have the RecNetLogin package installed, does the recnetlogin folder exist?''')

''' Just Initializing some values '''
login = rnl.login_to_recnet(username=user,password=passwd)
x = 0
BToken = ''

''' Initial token request '''
BToken = login.access_token

print(BToken)

''' The loop program that actually makes the picure move '''
while 1 == 1:
    
    ''' The HTTP header for changing your In-Game pfp '''
    Headers = {'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="88"',
          'Accept' : '*/*',
          'sec-ch-ua-mobile' : '?0',
          'Authorization' : BToken,
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
          'Origin' : 'https://rec.net',
          'Sec-Fetch-Site' : 'same-site',
          'Sec-Fetch-Mode' : 'cors',
          'Sec-Fetch-Dest' : 'empty',
          'Referer' : 'https://rec.net/',
          'Accept-Encoding' : 'gzip, deflate',
          'Accept-Language' : 'en-US,en;q=0.9',
          'User-Agent' : 'Bugcrowd-Testing',
          }    
    
    ''' Requests a new auth token when that one is no longer valid '''
    r = requests.get('https://accounts.rec.net/account/me/', headers = Headers)

    if r.status_code == 401:
        print('Invalid Token')
        login = rnl.login_to_recnet(username=user,password=passwd)
        BToken = login.access_token

        print(BToken)
