import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import json
import string
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
        name.append(i + str(idx))

    for i in pw:
        idx = abet.index(i)
        i = rabet[idx]
        pasw.append(i + str(idx))
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

#print(encrypt('srijan','dhungana'))
print(decrypt('h18i17r8q9z0m13','w3s7f20m13t6z0m13z0'))








'''class Grid(Widget):

    def __init__(self):
        abet = list(string.ascii_lowercase)
        rabet = list(string.ascii_lowercase)
        rabet.sort(reverse = True)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def normal(self, instance):
        self.ids.signin.text = 'sign in'
        self.ids.submit.text = 'submit'
    def normalize(self):
        Clock.schedule_once(self.normal, 1)
    def content(self,file):
        with open(file, 'r') as f:
            data = json.load(f)

        return data

    def save(self):
        file = 'verification.json'
        verification = {'name' : self.username.text.lower(), 'pass' : self.password.text.lower()}
        print(verification)
        if self.username.text and self.password.text:
            self.ids.signin.text = 'sign in'
            self.ids.submit.text = 'submit'
            try :
                data = self.content(file)

            except:
                with open (file, 'w') as f:
                    json.dump([verification], f)
                self.content(file)
            else:
                if verification not in data:
                    with open('verification.json','w') as f:
                        data.append(verification)
                        json.dump(data, f)
                        self.ids.submit.text = 'done'
                else:
                    self.ids.submit.text = 'you already have an account'

        else:
            self.ids.submit.text = 'nope sir'
    def load(self):
        file = 'verification.json'
        verification = {'name' : self.username.text, 'pass': self.password.text}

        try:
            data = self.content(file)
            print(data)
        except:
            self.ids.signin.text = ' submit first'

        else:
            for i in data:
                if i['name'] == self.username.text and i['pass'] == self.password.text:
                    self.ids.signin.text = 'youre in'
                    no = False
                    break
                else:
                    no = True
            if no:
                self.ids.signin.text = 'nope sir'



    pass


class MyApp(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    MyApp().run()'''
