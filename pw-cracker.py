import hashlib
from itertools import combinations
from string import ascii_letters, digits, punctuation

#common passwords
def crackCommon(hashPass):
    currWord = ''
    f = file("/usr/share/dict/commonWords.txt").read()

    for word in f.split():
        if(hashlib.sha256(word).hexdigest() == hashPass):
                currWord = word;
                break;
    return currWord;


#passwords that begin with special character
def crackSpecialChar(hashPass):
    currWord = ''

    for symbol in ['!','~','*','#']:
        for letter in ascii_letters:
            for letter2 in ascii_letters:
                for letter3 in ascii_letters:
                    word = symbol+letter+letter2+letter3
                    if(hashlib.sha256(word).hexdigest() == hashPass):
                        currWord = word;
                        break;
    
    for symbol in ['!','~','*','#']:
        for letter in ascii_letters:
            for letter2 in ascii_letters:
                for letter3 in digits:
                    word = symbol+letter+letter2+letter3
                    if(hashlib.sha256(word).hexdigest() == hashPass):
                        currWord = word;
                        break;
     
    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in digits:
                for letter2 in ascii_letters:
                    for letter3 in ascii_letters:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;

    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in ascii_letters:
                for letter2 in digits:
                    for letter3 in ascii_letters:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;
      

    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in digits:
                for letter2 in digits:
                    for letter3 in digits:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;
    
    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in digits:
                for letter2 in ascii_letters:
                    for letter3 in digits:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;
      
    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in digits:
                for letter2 in digits:
                    for letter3 in ascii_letters:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;

    if(currWord == ''):
        for symbol in ['!','~','*','#']:
            for letter in ascii_letters:
                for letter2 in digits:
                    for letter3 in digits:
                        word = symbol+letter+letter2+letter3
                        if(hashlib.sha256(word).hexdigest() == hashPass):
                            currWord = word;
                            break;
     
    
    return currWord
#length 7 words from words wordlist
def crackWordList7(hashPass):
    currWord = ''

    f = file("/usr/share/dict/words.txt").read()
    for word in f.split():
        if(len(word) == 7):
            word = word[0].upper() + word[1:]
            for num in digits:
                wordnum = word + num
                if(hashlib.sha256(wordnum).hexdigest() == hashPass):
                    currWord = wordnum;
                    break
                else:
                    wordnum = word

    return currWord;
#length 5 words from words wordlist
def crackWordList5(hashPass):
    currWord = ''

    f = file("/usr/share/dict/words.txt").read()
    for word in f.split():
        if(len(word) == 5):
            if('a' in word):
                word = subA(word)
            if('l' in word):
                word = subL(word)
            if(hashlib.sha256(word).hexdigest() == hashPass):
                 currWord = word;
                 break

    return currWord;
#substitute a for @
def subA(word):
    res_list = [i for i in range(len(word)) if word[i] == 'a']
    
    for x in res_list:
        lst = list(word)
        lst[x] = '@'
        word = "".join(lst)
    
    return word
#substitute l for 1
def subL(word):
    res_list = [i for i in range(len(word)) if word[i] == 'l']
    
    for x in res_list:
        lst = list(word)
        lst[x] = '1'
        word = "".join(lst)
    
    return word

#word list in share folder
def anyNumFromWords(hashPass):
    currWord = ''
    f = file("/usr/share/dict/words.txt").read()
    for word in f.split():
        if(hashlib.sha256(word).hexdigest() == hashPass):
                currWord = word;
                break;
    return currWord;

#brute force to find passwords for length 6
def brute6(hashPass):
    currWord = ''
    lst = list(ascii_letters + digits + punctuation)
    rawCombos = combinations(lst,6)
    combos = []
    for i in rawCombos:
        combos.append(''.join(i))
        if(hashlib.sha256(combos[-1]).hexdigest() == hashPass):
            currWord = combos[-1]
            break
        else:
            currWord = ''
    return currWord


############## MAIN PROGRAM ##########################
print "Hello, Welcome to Johnneisha's Password Cracker!"
print "Please enter the name of your input file: "
filename = raw_input()
print "Great! If the password is cracked, it will appear in a file called crackedpasswords.txt"
f = open(filename,"r")

pwdfile = open("crackedpasswords.txt", "a")
with open (filename, 'r') as f:
    for entry in f:
    #split input
        colon = entry.index(":")
        noUsername = entry[colon+1:]
        if(":" in noUsername):
             otherstuff = noUsername.index(":")
             password = entry[colon+2:otherstuff+6]
        else: 
            password = noUsername
    
    #run crackers
        if crackCommon(password) != '':
            pwdfile.write(entry[:colon] + ":" +crackCommon(password) + "\n")
            print ("Complete!")
            break
        elif anyNumFromWords(password) != '':
            print "Still running..."
            pwdfile.write(entry[:colon] + ":" + anyNumFromWords(password) + "\n")
            print ("Complete!")
            break
        elif crackSpecialChar(password) != '':
            print "Still running..."
            pwdfile.write(entry[:colon] + ":" + crackSpecialChar(password) + "\n")
            print ("Complete!")
            break
        elif crackWordList5(password) != '':
            print "Still running..."
            pwdfile.write(entry[:colon] + ":" + crackWordlist5(password) + "\n")
            print ("Complete!")
            break
        elif crackWordList7(password) != '':
            print "Still running..."
            pwdfile.write(entry[:colon] + ":" + crackWordlist7(password) + "\n")
            print ("Complete!")
            break
        elif brute6(password) != '':
            print "Still running..."
            pwdfile.write(entry[:colon] + ":" + brute6(password) + "\n")
            print ("Complete!")
            break
        else: 
            print "Sorry! I could not crack this password :-("
   
pwdfile.close()

