

def lookup(searchterm):
    print('looking up ' + searchterm)
    if (len(searchterm) == 0):
        return ('Tell me what to look for, and I shall deliver.')
    array = searchterm.split(' ')
    print(array)
    if(len(array) < 2):
        set1 = parseset(array[0])
        if(set1 is None):
            return 'Could not understand ' + array[0] + ', try again'
        response = "http://elsgear.com/ib/set/" + str(set1) + "/1"
        print(response)
        return(response)
    else:
        arg1 = array[0]
        arg2 = array[1]
        print(arg1)
        print(arg2)
        char1 = parsecharacter(arg1)
        set1 = parseset(arg1)
        char2 = parsecharacter(arg2)
        set2 = parseset(arg2)
        if((char1 is None) and (set1 is None)):
            return 'Could not understand ' + arg1 + ', try again'
        elif((char2 is None) and (set2 is None)):
            return 'Could not understand ' + arg2 + ', try again'
        elif((char1 is None) and (set2 is None)):
            print(set1, char2)
            response = "http://elsgear.com/ib/set/" + str(set1) + "/" + str(char2)
            print(response)
            return(response)
        elif((char2 is None) and (set1 is None)):
            print(set1, char2)
            response = "http://elsgear.com/ib/set/" + str(set2) + "/" + str(char1)
            print(response)
            return(response)
        else:
            return 'I could not understand your inquiry. Please try again.'


def parsecharacter(string):
    if(string.lower() == 'elboy' or string.lower() == 'elsword'):
        return 1
    elif(string.lower() == 'aisha'):
        return 2
    elif(string.lower() == 'rena'):
        return 3
    elif(string.lower() == 'raven'):
        return 4
    elif(string.lower() == 'eve'):
        return 5
    elif(string.lower() == 'chung'):
        return 6
    elif(string.lower() == 'ara'):
        return 7
    elif(string.lower() == 'elesis'):
        return 8
    elif(string.lower() == 'add'):
        return 9
    elif(string.lower() == 'lu'):
        return 10
    elif(string.lower() == 'ciel'):
        return 11
    else:
        return None

def parseset(string):
    if(string.upper() == 'AA'):
        return 1
    elif(string.upper() == 'EO'):
        return 2
    elif(string.upper() == 'NBS'):
        return 3
    elif(string.upper() == 'AD'):
        return 4
    elif(string.upper() == 'SS'):
        return 5
    elif(string.upper() == 'VIG'):
        return 6
    elif(string.upper() == 'RS' or string.upper() == 'RM' or string.upper() == 'RSR' or string.upper() == 'RMR'):
        return 7
    elif(string.upper() == 'ET'):
        return 8
    elif(string.upper() == 'SD'):
        return 9
    elif(string.upper() == 'SI'):
        return 10
    elif(string.upper() == 'GF'):
        return 11
    elif(string.upper() == 'DY' or string.upper() == 'HDY'):
        return 12
    elif(string.upper() == 'RB'):
        return 13
    elif(string.upper() == 'DK' or string.upper() == 'DKA' or string.upper() == 'DKDS'):
        return 14
    elif(string.upper() == 'HU'):
        return 15
    elif(string.upper() == 'DS' or string.upper() == 'PS'):
        return 16
    elif(string.upper() == 'SE'):
        return 17
    elif(string.upper() == 'GP' or string.upper() == 'GLACIAL'):
        return 18
    elif(string.upper() == 'GOF'):
        return 19
    elif(string.upper() == 'MK2' or string.upper() == 'MKB'):
        return 20
    elif(string.upper() == 'SV'):
        return 21
    elif(string.upper() == 'IGC'):
        return 22
    elif(string.upper() == 'ETS2'):
        return 23
    elif(string.upper() == 'HNO' or string.upper() == 'HNOR'):
        return 24
    elif(string.upper() == 'TH' or string.upper() == 'TT' or string.upper() == 'TDI'):
        return 25
    elif(string.upper() == 'MA'):
        return 26
    elif(string.upper() == 'MF'):
        return 27
    elif(string.upper() == 'SG'):
        return 28
    elif(string.upper() == 'VAK' or string.upper() == 'VBN'):
        return 29
    elif(string.upper() == 'MQ' or string.upper() == 'MASQUERADE'):
        return 30
    else:
        return None