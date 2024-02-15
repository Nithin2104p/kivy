from kivy import *
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='NIVI', font_size=32)
        button.bind(on_press=self.button_pressed)
        return button

    def button_pressed(self, instance):
        import nivi as neural_vision 
        neural_vision()
       
if __name__ == "__main__":
    MyApp().run()
