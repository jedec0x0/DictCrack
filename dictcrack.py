import crypt

def tryPass(unixpass):
    salt = unixpass[0:2]
    dictFile = open('dictfile.txt','r')
    for word in dictFile.readline():
        word = word.strip('\n')
        cryptword = crypt.crypt(word,salt)
        if (cryptword == unixpass):
            print "[+] Cracked Password: " + word + "\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('passfile.txt')
    for line in passFile.readlines():
        if ":" in line: #to clean up the ':' characters
            user = line.split(':')[0]
            unixpass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: " + user
            tryPass(unixpass)

if __name__ == "__main__":
    main()
