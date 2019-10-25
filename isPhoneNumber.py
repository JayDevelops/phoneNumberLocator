#REMEMBER, STRINGS START AT 0!!!
def isPhoneNumber(text):
    #If the length of the string isn't 12, automatically return false
    if len(text) != 12:
        return False
    #Checks the first three digits to make sure it isn't a decimal
    for num in range(0,3):
        if not text[num].isdecimal():
            return False
    #If the third position isn't a dash, return false
    if text[3] != "-":
        return False
    #Now checks the next three positions, doesn't include the seventh position
    for num in range(4,7):
        if not text[num].isdecimal():
            return False
    #If the seventh position isn't a dash, return false
    if text[7] != "-":
        return False
    #Now checks the last three postions, doesn't include the eleventh postion
    for num in range(8, 12):
        if not text[num].isdecimal():
            return False
    return True


message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
for eachTwelveCharacterLength in range(len(message)):
    #Iterates at the 0 index, then keeps adding 1 to the next character, then examining the message in twelve characters at a time!
    #It calls to the function called isPhoneNumber as a condition
    chunkText = message[eachTwelveCharacterLength: eachTwelveCharacterLength + 12 ]
    if isPhoneNumber(chunkText):
        print("Phone Number Found:", chunkText )
print("done")
