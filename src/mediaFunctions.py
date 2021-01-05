# Must import python's requests library and the custom query.
import requests
from grabTopMedia import grabTopMediaQuery

# Function to have the user decide if they want to view their top rated anime or manga w/ error handling.
def chooseType():
    # two defaults before entering while
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

    return userType

def getTopMedia():

    # variables fed in by the user to grab their info
    variables = {
        'name': input("Enter your Anilist username: ").strip(),
        'chosenType': chooseType()
    }
    # anilist api url and grabbing the response.
    url = 'https://graphql.anilist.co'
    # query used from the grabTopMedia file.
    response = requests.post(url, json={'query': grabTopMediaQuery, 'variables': variables})

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
                print("\"" + entry['media']['title']['romaji'] + "\" with a score of: " + str(entry['score']))
    elif response.status_code == 404:
        print("Could not find your Anilist Profile.")