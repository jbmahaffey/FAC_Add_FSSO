import requests, ssl

def main():
    user = 'admin'
    # Add api key for user
    apikey = ''
    url = 'https://192.168.101.45/api/v1/ssoauth/'
    headers = {
            'content-type': 'application/json'
            }
    
    data = {
        "event":"1",
        "username":"cwindsor",
        "user_ip":"10.1.73.175"
    }

    resp = requests.post(url=url, headers=headers, auth=(user, apikey), json=data, verify=False)
    print(resp.status_code)


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    requests.packages.urllib3.disable_warnings() 
    main()