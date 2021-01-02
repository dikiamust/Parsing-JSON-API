#SCRAPING ACCOUNTS (USER NAME, FULL NAME & PROFILE PICT) THAT LIKED ON AN INSTGRAM POST
#SCRAPING AKUN (USER NAME, FULL NAME & PROFILE PICT) YANG MENYUKAI DI POSTINGAN INSTGRAM

import requests, json

url ='https://www.instagram.com/graphql/query'

short_code = input(' Please input a short code: ')

varibles = {"shortcode":short_code,"first":50}

headers = {'cookie' : 'sessionid=35446217166%3AOQUzieUlH1aSvO%3A14'}

params = {
    'query_hash' : 'd5d763b1e2acf209d62d22d184488e57',
    'variables' : json.dumps(varibles)
}

r = requests.get(url, headers=headers, params=params).json()
users = r['data']['shortcode_media'] ['edge_liked_by'] ['edges']

count = 0
for user in users:
    username = user ['node']['username']
    full_name = user ['node']['full_name']
    profile_pic = user ['node']['profile_pic_url']
    print(username, full_name, profile_pic)
    count+=1
    print(count)
