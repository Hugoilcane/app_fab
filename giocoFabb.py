from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
import time

class ComunicaArduino(Screen):
    def __init__(self, **kwargs):
        super(ComunicaArduino,self).__init__(**kwargs)
        self.window=BoxLayout(orientation='vertical', spacing=10)
        self.window.size_hint=(0.8,0.8)
        self.add_widget(Image(source="sfondo_appFabb.jpeg", allow_stretch=True, keep_ratio=False))
        Window.size=(360,640)
        self.window.pos_hint={'center_x':0.5, 'center_y':0.7}
        self.sound=SoundLoader.load("buzzer.mp3")
        self.window.add_widget(TextInput(
            font_size='22sp',
            size_hint=(None,None),
            size=(300,100),
            hint_text="quale patatine mi piacciono di più tra patatine alla paprika e patatine al salame?",
            readonly=True)
            )
        self.testo=TextInput(
            font_size='20sp',
            padding_y='12sp',
            size_hint=(None,None),
            size=(300,100),
            foreground_color=(1,0,0,1),
            halign='center',
            hint_text="inserisci il testo"
            )
        self.window.add_widget(self.testo)
        self.bottone=Button(
            font_size='20sp',
            text="vai alla seconda pagina",
            size_hint=(None,None),
            size=(210,100),
            background_color=(1,0,0,0.5),
            color=(0,0,0,1),
            pos_hint={'center_x':0.5, 'center_y':0.5},
            on_press=self.ControlloRisposta
            )
        self.window.add_widget(self.bottone)
        self.add_widget(self.window)
        
    def ControlloRisposta(self, instance):
        data=self.testo.text
        if(data=="hi"):
            self.Schermata_2(instance)
        else:
            self.testo.text="errore"
            if self.sound:
                self.sound.volume=0.5
                self.sound.play()            
        
    def Schermata_2(self, instance):
        self.manager.current="second"

class SecondPage(Screen):
    def __init__(self,**kwargs):
        super(SecondPage,self).__init__(**kwargs)
        loyaut=BoxLayout(orientation='vertical')
        loyaut.add_widget(Button(text="torna alla prima pagina", on_press=self.ControlloRisposta_2))
        self.add_widget(loyaut)
    
    def ControlloRisposta_2(self, instance):
        data=self.testo.text
        if(data=="hi"):
            self.go_to_first_page(instance)
        else:
            self.testo.text="errore"
            if self.sound:
                self.sound.volume=0.5
                self.sound.play()
        
    def go_to_first_page(self,instance):
        self.manager.current="home"
            
class MyScreenManager(ScreenManager):
    pass
            
class App_principale(App):
    def build(self):
        self.icon="icon_appFabb.png"
        self.title="FABAPP"
        sm = MyScreenManager()
        sm.add_widget(ComunicaArduino(name="home"))  # Aggiungi la schermata home
        sm.add_widget(SecondPage(name="second"))  # Aggiungi la schermata second
        return sm
    
        
App_principale().run()  