import json
import sys

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

from enc_n_dec import decrypt, encrypt

Builder.load_file('my.kv')


class Menu(Screen):


    suusername = ObjectProperty(None)
    supassword = ObjectProperty(None)
    sipassword = ObjectProperty(None)
    siusername = ObjectProperty(None)

    def normal(self, instance):
        self.ids.signin.text = 'sign in'
        self.ids.submit.text = 'submit'
    def normalize(self):
        Clock.schedule_once(self.normal, 2)
    def content(self,file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    def save(self):
        file = 'verification.json'
        verification = encrypt(self.suusername.text.lower().strip(),self.supassword.text.lower().strip())
        if self.suusername.text and self.supassword.text:
            self.ids.signin.text = 'sign in'
            self.ids.submit.text = 'submit'
            try :
                data = self.content(file)
            except:
                with open (file, 'w') as f:
                    json.dump([verification], f)
                    self.ids.submit.text = 'done'
            else:
                for i in data:
                    usps = decrypt(i['name'], i['pass'])
                    if usps['name'] == self.suusername.text.strip() and usps['password'] == self.supassword.text.strip():
                        self.ids.submit.text = 'you already have an account'
                        flg = False
                        break
                    else:
                        flg = True
                        pass

                if flg:
                    with open(file,'w') as f:
                        data.append(verification)
                        json.dump(data, f)
                        self.ids.submit.text = 'done'

        else:
            self.ids.submit.text = 'nope sir'
    def load(self):
        file = 'verification.json'
        verification = decrypt(self.siusername.text,self.sipassword.text)

        try:
            data = self.content(file)
            print(sys.getsizeof(data))
        except:
            self.ids.signin.text = ' submit first'

        else:
            for i in data:
                usps = decrypt(i['name'], i['pass'])

                if usps['name'] == self.siusername.text.strip() and usps['password'] == self.sipassword.text.strip():
                    self.ids.signin.text = 'youre in'
                    self.manager.current = 'main'
                    break
                else:
                    self.ids.signin.text = 'nope sir'

    pass
class Manager(ScreenManager):
    pass

class Sample(Screen):
    pass



class MyApp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    MyApp().run()
