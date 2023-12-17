from random import randint


def URLSHORT():
    #* step 1: Sett values 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SHORT = str()
    length = len(string)

    #* step 2: Text length is random & return OTP value
    for i in range(randint(6, 25)):
        SHORT += string[randint(0, length-1)]
    
    return SHORT
