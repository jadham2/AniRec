import requests

def getAbout():
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

def printAbout(response):
    if response.status_code == 200:
        json_resp = response.json()
        if json_resp['data']['User']['about'] is None:
            print("Could not find an about, but your name is: " + json_resp['data']['User']['name'])
        else:
            print('Your name is: ' + json_resp['data']['User']['name'] + '\nand your about is: ' + json_resp['data']['User']['about'])
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")

def getTopMedia():
    query = '''
        query ($name: String) {
            User (name: $name) {
                name
            }
            MediaList (userName: $name, sort: SCORE_DESC, status: COMPLETED) {
                media {
                    title {
                        romaji
                    }
                }
                score
            }
        }
        '''

    userName = input("Enter your Anilist username: ")
    variables = {
        'name' : userName.strip()
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})

    return response

def printTopMedia(response):
    if response.status_code == 200:
        json_resp = response.json()
        if json_resp['data']['MediaList'] is None:
            print("Could not find a rated Anime / Manga.")
        else:
            print('Your name is: ' + json_resp['data']['User']['name'] + '\nand your top rated Anime/Manga is: ' + json_resp['data']['MediaList']['media']['title']['romaji'] + " with a score of " + str(json_resp['data']['MediaList']['score']) + ".")
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")

def main():
    #TODO: Let a user filter by anime / manga, grab a list of the top 10.
    response = getTopMedia()
    printTopMedia(response)

if __name__ == '__main__':
    main()