# query with pagination to grab the user's top 10 media entries.
# TODO: Handle where the user doesn't have 10 entries / devise a better way to get their favorite media.
grabTopMediaQuery = '''
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