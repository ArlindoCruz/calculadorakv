from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class app (App):
    def build(self):

        coiso = BoxLayout(orientation = ('vertical'))
    
        texto1 = Label(text = 'olá senai', font_size = ('50pt'))
    
        texto2 = Label(text = 'olá sesi', font_size = ('50'), color= (1,0,0,1))
    
        coiso.add_widget(texto1)
        coiso.add_widget(texto2)
        return coiso
    
if __name__ == '__main__':
    app().run()
   

