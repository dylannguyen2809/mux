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


    


