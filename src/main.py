import mediaFunctions

def main():
    response = mediaFunctions.getTopMedia()
    mediaFunctions.printTopMedia(response)

if __name__ == '__main__':
    main()