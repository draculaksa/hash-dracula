import os
import time


print("""

 _               _               _                      _       
| |__   __ _ ___| |__         __| |_ __ __ _  ___ _   _| | __ _ 
| '_ \ / _` / __| '_ \ _____ / _` | '__/ _` |/ __| | | | |/ _` |
| | | | (_| \__ \ | | |_____| (_| | | | (_| | (__| |_| | | (_| |
|_| |_|\__,_|___/_| |_|      \__,_|_|  \__,_|\___|\__,_|_|\__,_|


                                                                

""")


hashh = raw_input("hash                 :")

types = raw_input("types                :")

wordlist = raw_input('wordlist (y or n)    :')



file = open('hash.txt', 'w')
file.write(hashh)
file.close()

time.sleep(2)

def hash_kill() :
    if wordlist == 'n':
        if types == 'md5' :
            os.system('hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a?a?a?a -i')

        if types == 'sha1' :
            os.system('hashcat -m 100 -a 3 hash.txt ?a?a?a?a?a?a?a?a?a -i')
    elif wordlist == 'y':
        wordlist1 = raw_input('wordlist             :')
        if types == 'md5':
            os.system('hashcat -m 0 -a 0 hash.txt {}  '.format(wordlist1))

        if types == 'sha1':
            os.system('hashcat -m 100 -a 0 hash.txt {} '.format(wordlist1))




hash_kill()
