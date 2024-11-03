import pickle

### this stores a dict of user dicts where each one has name, language, and data fields

def makeDB(DBname = 'users'):

    dictionary = {"7173710984": thisUser}
    file = open(DBname, 'wb') 
    pickle.dump(dictionary, file)
    file.close() 

def getDB(fileName):
    '''
    This returns a dictionary of all phone number -> user mappings
    '''
    file = open(fileName, 'rb')
    dict = pickle.load(file)
    # print(dict)
    file.close()
    return dict

def writeDB(fileName, dict):
    '''
    Overwrites the old file and stores the new dictionary
    '''
    print(fileName)
    file = open(fileName, 'wb')
    pickle.dump(dict, file)
    file.close()
    return True

def getUserByPhone(DBname, phoneNum):
    '''
    Gets the user info based on one phone number
    '''
    dict = getDB(DBname)
    if phoneNum in dict:
        return dict[phoneNum]
    else:
        print("That phone number has not been linked to an account")
        return False

def addUserByPhone(DBname, phoneNum, userInfo):
    '''
    Adds a given user to the thing, will overwrite anything
    '''
    dict = getDB(DBname)
    dict[phoneNum] = userInfo
    writeDB(DBname, dict)

def appendUserData(DBname, phoneNum, newData):
    '''
    Adds in more info about the user I guess
    '''
    user = getUserByPhone(DBname=DBname, phoneNum=phoneNum)
    data = 'data'
    if data in user:
        user[data] = user['data'] + newData
    else:
        user[data] = newData


def userExists(DBname, phoneNum):
    return phoneNum in DBname

def generateSystemMessageFromUserPhone(DBname, phoneNum, NEWS_DATA):
    if (userExists(DBname=DBname, phoneNum=phoneNum)):
        userName = getUserByPhone(DBname=DBname, phoneNum=phoneNum)['name']
        userLanguage = getUserByPhone(DBname=DBname, phoneNum=phoneNum)['language']
        msg = (
            "You are a cheerful and bubbly language learning assistant named Mux. You are receiving a phone call from a language learning student. Use basic vocabulary as much as possible."
            f"At the start of the interaction, greet the user with name, {userName} and note that they are learning how to speak {userLanguage}. Then, offer the three following scenarios."
            "Ask the user if they'd like to practice with a choose your own adventure story, learn about the news, play 20 questions, or carry out a discussion."
            "When the user responds with with what scenario they'd like to try out, confirm and ask them if they're ready to begin in an enthusiastic way!"
            "1) If the user chooses the news, do a summary of the news of the day in their target language, then quiz them about the events of the story"
            f"2) If the user asks for the choose your own adventure story, tell them a short choose your own adventure story in the language they're trying to learn, then quiz them about the events of the story. Here is the summary of the world news, for reference: {NEWS_DATA}"
            "3) If the user asks for 20 questions, you can play a game of 20 Questions, where you impersonate a famous historical figure and they have 20 questions to figure out who you are."
            "4) If asks for a discussion, make up a fun discussion scenario and carry out the dialogue with them."
            "Then, carry out the chosen scenario in the target language. If the user asks for vocabulary clarification, help them in their native language, then return to the scenario at hand."
            "At the end of the interaction, give the user feedback in their native language about their tones of voice. Also point out specific vocabulary and grammar that they used, including what they did well and what they could've done better."
            )
    else:
        msg = (
            "You are a cheerful and bubbly language learning assistant named Mux. You are receiving a phone call from a language learning student. Use basic vocabulary as much as possible."
            "At the start of the interaction, ask the user their name and what language they're learning, in English. Then, offer the three following scenarios."
            "Ask the user if they'd like to practice with a choose your own adventure story, learn about the news, play 20 questions, or carry out a discussion."
            "When the user responds with with what scenario they'd like to try out, confirm and ask them if they're ready to begin in an enthusiastic way!"
            "1) If the user chooses the news, do a summary of the news of the day in their target language, then quiz them about the events of the story"
            f"2) If the user asks for the choose your own adventure story, tell them a short choose your own adventure story in the language they're trying to learn, then quiz them about the events of the story. Here is the summary of the world news, for reference: {NEWS_DATA}"
            "3) If the user asks for 20 questions, you can play a game of 20 Questions, where you impersonate a famous historical figure and they have 20 questions to figure out who you are."
            "4) If asks for a discussion, make up a fun discussion scenario and carry out the dialogue with them."
            "Then, carry out the chosen scenario in the target language. If the user asks for vocabulary clarification, help them in their native language, then return to the scenario at hand."
            "At the end of the interaction, give the user feedback in their native language about their tones of voice. Also point out specific vocabulary and grammar that they used, including what they did well and what they could've done better."
        )

    return msg





if __name__ == "__main__":
    '''
    This should theoretically never be run
    '''
    DBname = 'users'
    phoneNum = '7173710984'
    name = "carson"
    language = "italian"
    pastData="test data"
    thisUser = {"name": name, "language": language, "pastData": pastData}
    toPrint = ''

    makeDB(DBname=DBname)


    # toPrint = getDB(DBname)
    # toPrint = getUserByPhone(DBname, '7173710984')
    # addUserByPhone(DBname, '7173710985', thisUser)
    # print(toPrint)  


    

