import requests

def getResponse():
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

    return response

def printResponse(response):
    if response.status_code == 200:
        json_resp = response.json()
        if json_resp['data']['User']['about'] is None:
            print("Could not find an about, but your name is: " + json_resp['data']['User']['name'])
        else:
            print('Your name is: ' + json_resp['data']['User']['name'] + '\nand your about is: ' + json_resp['data']['User']['about'])
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")

def main():
    response = getResponse()
    printResponse(response)

if __name__ == '__main__':
    main()