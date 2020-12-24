import requests

if __name__ == '__main__':
    query = '''
    query ($name: String) {
        User (name: $name) {
            name
            about
        }
    }
    '''

    userName = input("Enter your Anilist username: ")

    variables = {
        'name': userName.strip()
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})

    if response.status_code == 200:
        json_resp = response.json()
        print('Your name is: ' + json_resp['data']['User']['name'] + '\nand your about is: ' + json_resp['data']['User']['about'])
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")