from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class HackApp(App):

    def build(self):
        self.title = "HackApp"

        mainwindow = BoxLayout()
        popupbutton = Button(text="Choose the photo to analyse", size_hint=(0.5, 0.5))
        popup = Popup(size_hint=(0.5, 0.5))
        chooser = FileChooserIconView()

        popupbutton.bind(on_press=popup.open)

        popup.add_widget(chooser)
        mainwindow.add_widget(popupbutton)

        return mainwindow

if __name__ == '__main__':
    HackApp().run()