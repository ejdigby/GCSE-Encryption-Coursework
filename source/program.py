import random

## Define Generate Key Function
def GenerateKey():
    chctkey = ""
    for i in range(8):
        x = chr(random.randrange(33,127))
        chctkey += x
    return chctkey

##Determine Off set factor
def CalcOffset(key):
    offset = 0
    for i in key:
        x = ord(i)
        offset += x
    offset = round(offset / 8) - 32
    return offset

## Define Encrypt Text Function
def EncryptText(text, offset):
    finaltext = ""
    text = text.strip()
    for c in text:
        x = c
        if x == " ":
            finaltext += " "
        else:
            x = ord(c) + offset
            if x > 126:
                x -= 94
            x = chr(x)
            finaltext  += x
    return finaltext

## Define Secure Encrypt Text Function
def SecureEncryptText(text, offset):
    finaltext = ""
    text = text.strip()
    text = text.replace(" ", "")
    chct = 0
    for c in text:
        chct = chct + 1
        x = c
        x = ord(c) + offset
        if x > 126:
           x -= 94
        x = chr(x)
        finaltext  += x
        if chct % 5 == 0:
            finaltext += " "
    return finaltext

## Define the Decrypt Function
def DecryptText(text, offset):
    finaltext = ""
    for c in text:
        x = c
        if x == " ":
            finaltext += " "
        else:
            x = ord(c)
            x = x - offset
            if x < 33:
                x = x + 94
            x = chr(x)
            finaltext  += x
    print(finaltext)
    return finaltext

## Function to write a files
def writefile(Text):
    filesaved = False
    while filesaved == False:
        FileName = input("What would you like to save the encrypted file as? ")
        if FileName.strip() ==  "" or FileName.strip() == ".txt":
            filesaved = False
            print ("Please enter a valid file name")
        else:
            if FileName.endswith(".txt"):
                pass
            else:
                FileName += ".txt"
            try:
                f = open(FileName, "w")
                f.write(Text)
                f.close()
                print("File Written at: " + FileName)
                filesaved = True
                return
            except:
                print ("Sorry there was an error saving your file. Please try again")
                filesave = False

## Function to read a file
def readfile(FileName):
    print(FileName)
    fileloaded = False
    sure = "NULL"
    while fileloaded == False:
        try:
            f = open(FileName, "r")
            text = f.read()
            print(text)
            f.close()
            if FileName.endswith(".txt"):
                fileloaded = True
                while sure != "YES" or sure != "NO":
                    sure = input("Is this the file: " +  FileName + " you want to open? [Yes / No]")
                    sure = sure.upper()
                    if sure == "YES" or sure == "Y":
                        print ("File Loaded!")
                        return text
                    elif sure == "NO" or sure == "N":
                        fileloaded = False
                        FileName = input("What file would you like to open?")
                    else:
                        print ("Please enter Yes or No")
            else:
               print ("Sorry that file isn't a txt file. Please try again")
               fileloaded = False
               FileName = input("What file would you like to open?")
        except:
            if FileName.endswith(".txt"):
                print("File Not Found")
            else:
                print ("Sorry that file isn't a txt file. Please try again")
            fileloaded = False
            FileName = input("What file would you like to open?")

##Function to print the main menu
def mainmenu():
    ## Define choice as null
    choice = "NULL"
    choices = ["A", "B", "C", "D"]
    print ("Main Menu")
    print ("A - Encrypt")
    print ("B - Secure Encrypt")
    print ("C - Decrypt")
    print ("D - Exit")

    ##While no choice has been selected
    while choice != choices:
        choice = input("Please choose and option: ")
        choice = choice.upper()
        if choice == choices[0]:
            encrypt()
        elif choice == choices[1]:
            secureencrypt()
        elif choice == choices[2]:
            decrypt()
        elif choice == choices[3]:

            sure = input("Are You Sure? [Yes/No]")
            sure = sure.upper()
            print (sure)
            if sure == "YES":
                print("Goodbye")
                exit()
            else:
                choice = "NULL"
        else:
            print (choice, "is not recongised")
            print ("Please try again")
            choice = "NULL"



## Main Encrypt Function
def encrypt():
    filename = input("What file would you like to open?")
    filetext = readfile(filename)
    key = GenerateKey()
    print ("Your Key Is: ", key)
    print ("Do Not Forget This Key")
    offsetfactor = CalcOffset(key)
    EText = EncryptText(filetext, offsetfactor)
    writefile(EText)

def secureencrypt():
    filename = input("What file would you like to open?")
    filetext = readfile(filename)
    key = GenerateKey()
    print ("Your Key Is: ", key)
    offsetfactor = CalcOffset(key)
    SEText = SecureEncryptText(filetext, offsetfactor)
    writefile(SEText)

## Main Decrypt Function
def decrypt():
    filename = input("What file would you like to open?")
    filetext = readfile(filename)
    key = input("What key was used to encrypt this text?")
    offsetfactor = CalcOffset(key)
    DText = DecryptText(filetext, offsetfactor)
    print (DText)


mainmenu()
