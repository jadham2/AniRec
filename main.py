import requests

def getTopMedia():
    # query with pagination to grab the user's top 10 media entries.
    # TODO: Handle where the user doesn't have 10 entries / devise a better way to get their favorite media.
    query = '''
        query ($name: String, $chosenType: MediaType) { 
            User (name: $name) {
               name
           }
            Page (page: 1, perPage: 10) {
                mediaList (userName: $name, type: $chosenType, sort: SCORE_DESC) {
                    media {
                        title {
                            romaji
                        }
                    }
                    score
                }
            }
        }
        '''

    # TODO: allow user to enter their username
    userName = 'SuccubusSenpai' #input("Enter your Anilist username: ")

    # Block of code with error handling to have the user decide if they want to view their top rated anime or manga
    isValidType = False
    userType = 'ANIME'
    while not isValidType:
        tempType = int(input("Type 1 for Anime or 2 for Manga: "))
        if tempType == 1:
            userType = 'ANIME'
            isValidType = True
        elif tempType == 2:
            userType = 'MANGA'
            isValidType = True
        else:
            print("Error! Invalid type. Please try again.")

    # variables fed in by the user to grab their info
    variables = {
        'name': userName.strip(),
        'chosenType': userType
    }
    # anilist api url and grabbing the response.
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})

    return response


def printTopMedia(response):
    # Check if the response had a valid code. If it returned 404, inform the user.
    if response.status_code == 200:
        json_resp = response.json()
        # check if the response could not find anime or manga that were rated.
        if json_resp['data']['Page']['mediaList'] is None:
            print("Could not find rated Anime / Manga.")
        else:
            # print the user's top 10 media.
            print('Your name is: ' + json_resp['data']['User']['name'] + '\nand your top rated Anime are: ')
            for entry in json_resp['data']['Page']['mediaList']:
                print(entry['media']['title']['romaji'] + " with a score of: " + str(entry['score']))
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")


def main():
    #TODO: Let a user filter by anime / manga, grab a list of the top 10.
    response = getTopMedia()
    printTopMedia(response)


if __name__ == '__main__':
    main()