import string
import random



abet = list(string.ascii_lowercase)
rabet = list(string.ascii_lowercase)
rabet.sort(reverse = True)
def encrypt(usr, pw):
    name = []
    pasw = []
    verification = {}
    usr = usr.lower()
    pw = pw.lower()
    for i in usr:
        idx = abet.index(i)
        i = rabet[idx]
        name.append(i + str(random.randint(0,1000)))

    for i in pw:
        idx = abet.index(i)
        i = rabet[idx]
        pasw.append(i + str(random.randint(0,1000)))
    verification['name'] = ''.join(name)
    verification['pass'] = ''.join(pasw)

    return verification

def decrypt(usr, psw):
    name = []
    pasw = []
    decrypted = {}
    usr = usr.lower()
    psw = psw.lower()
    for i in usr:
        try:
            idx = abet.index(i)
            i = rabet[idx]
            name.append(i)
        except ValueError:
            pass
        except Exception as e:
            print(e)

    for i in psw:
        try:
            idx = abet.index(i)
            i = rabet[idx]
            pasw.append(i)
        except ValueError:
            pass
        except exception as e:
            print(e)
    decrypted['name'] = ''.join(name)
    decrypted['password'] = ''.join(pasw)
    return decrypted
