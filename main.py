import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

import warnings
warnings.filterwarnings('ignore')

Window.clearcolor = (0.8, 0.8, 0.8, 0)
color_text = (0, 0, 0, 1)
color_button = (0.75, 0.75, 0.75, 1)


def predict(imgPath):
    classes_path = "./classe.txt"
    with open(classes_path, 'r') as f:
        classes = f.readlines()
        classes = list(map(lambda x: x.strip(), classes))

    img1 = image.load_img(imgPath, target_size=(64, 64))
    img = image.img_to_array(img1)
    img = img / 255
    img = np.expand_dims(img, axis=0)

    model = load_model("./model_fine_final.h5")

    prediction = model.predict(img, batch_size=None, steps=1)

    pourc_pred = max(prediction[0])
    ind_pred = prediction.argmax()

    # print(f'Classe : {classes[ind_pred]}')
    # print(f'Pourcentage de précision : {pourc_pred}')

    return classes[ind_pred], pourc_pred


class HackApp(App):

    def update(self, select, instance, value):
        file = self.chooser.selection
        self.imagebox.clear_widgets()
        selected = Image(source=file[0])
        self.imagebox.add_widget(selected)

        class_found, pourc = predict(file[0])
        self.resultlabel.text = f'Classe : {class_found}\nPourcentage : {pourc}'

    def build(self):
        self.title = "HackApp"
        mainwindow = BoxLayout(orientation="vertical")
        imagelayout = BoxLayout(orientation="vertical")
        resultlayout = BoxLayout()
        self.imagebox = BoxLayout()
        popupbutton = Button(text="Choose the photo to analyse", size_hint=(0.5, 0.2), pos_hint={'x': 0.25},
                             background_color=color_button)
        launchbutton = Button(text="Launch Analysis", size_hint=(0.5, 0.2), pos_hint={'x': 0.25},
                              background_color=color_button)
        popup = Popup(size_hint=(0.5, 0.5))

        ospath = os.path.abspath(os.getcwd())
        self.chooser = FileChooserIconView(path=ospath)

        self.resultlabel = Label(text="", color=color_text)

        ledimage = Image(source="led-sunlight-300x230.jpg")

        popupbutton.bind(on_press=popup.open)
        self.chooser.bind(on_submit=self.update)

        popup.add_widget(self.chooser)
        imagelayout.add_widget(self.imagebox)
        imagelayout.add_widget(popupbutton)
        imagelayout.add_widget(launchbutton)
        resultlayout.add_widget(self.resultlabel)
        resultlayout.add_widget(ledimage)
        mainwindow.add_widget(imagelayout)
        mainwindow.add_widget(resultlayout)

        return mainwindow


if __name__ == '__main__':
    HackApp().run()
