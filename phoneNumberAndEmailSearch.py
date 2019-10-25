#FINDS ALL PHONE NUMBERS AND EMAILS IN THE COPIED clipboard, SPITS IT OUT TO YOU

import re, pyperclip #Imports Regex and Pyperclip

print("Remember, you need the text copied before you run this script!\n")
#TODO: Create two regex for phone numbers and email

#The following gets an optional area code, the separator if any, first three digits, separator, last four digits, and extension if any
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)


# TODO: Create a email regex
# Follwowing searches the first a-z & A-Z without symbols, the @ symbol, then the domain name without a dash, then dot something
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)



#Pastes the clipboard text into this 'text' variable, as a string
text = str(pyperclip.paste())
matches = []


#TODO: Loops if there's any groups within the text.
#The first, third, and fifth group is added to the vairbale 'phoneNum' with the .join() method
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += ' x' + groups[8] #Adds the extension if possible at the end of the phoneNum
    matches.append(phoneNum) #Now it finally adds it to the matches array at the end, for all the numbers in the text

for groups in emailRegex.findall(text):
    matches.append(groups[0]) #Finds all the email regex chracters and appends it to the 'matches' array


# TODO: Copy the text back into the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) #Join all strings into one string
    print('Copied to clipboard:')
    print('\n'.join(matches))
    print("\n Paste wherever you like and enjoy!")
else:
    print('No phone numbers or email addresses found.')
