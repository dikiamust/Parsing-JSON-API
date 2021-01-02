#SCRAPING ACCOUNT (USER NAME, FULL NAME & PROFILE PICT) THAT LIKED ON AN INSTGRAM POST
#SCRAPING AKUN (USER NAME, FULL NAME & PROFILE PICT) YANG MENYUKAI DI POSTINGAN INSTGRAM

import requests, json, time

url ='https://www.instagram.com/graphql/query'

short_code = input(' Please input a short code: ')

end_cursor = ''

count = 0
while 1 :
    varibles = {
        "shortcode": short_code,
        "first": 500,
        "after": end_cursor
    }

    headers = {'cookie': 'sessionid=35446217166%3AOQUzieUlH1aSvO%3A14'}

    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps( varibles )
    }

    r = requests.get( url, headers=headers, params=params ).json()
    try: users = r['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for 10 secs')
        time.sleep(10)
        continue

    for user in users:
        username = user['node']['username']
        full_name = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count += 1
        print(count, username, full_name, profile_pic)


    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False : break
    time.sleep(2)




