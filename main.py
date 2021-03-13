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

import os
import math
import tensorflow
import numpy as np
import imghdr
import matplotlib.pyplot as plt
from random import randint
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import *
import warnings
warnings.filterwarnings('ignore')

Window.clearcolor = (0.8, 0.8, 0.8, 0)
color_text = (0, 0, 0, 1)
color_button = (0.75, 0.75, 0.75, 1)


def predict(path):
    classes_path = "./classe.txt"
    with open(classes_path, 'r') as f:
        classes = f.readlines()
        classes = list(map(lambda x: x.strip(), classes))
    num_classes = len(classes)

    #model = create_model()

    #model.compile(
    #    loss='binary_crossentropy',
    #    optimizer=Adam(lr=0.0001),
    #    metrics=['accuracy'])

    model = load_model("./model_fine_final.h5")
    model.summary()


class HackApp(App):

    def update(self, select, instance, value):
        file = self.chooser.selection
        self.imagebox.clear_widgets()
        selected = Image(source=file[0])
        self.imagebox.add_widget(selected)

    def build(self):
        self.title = "HackApp"
        predict('')
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

        resultlabel = Label(text="Stage 3", color=color_text)

        ledimage = Image(source="led-sunlight-300x230.jpg")

        popupbutton.bind(on_press=popup.open)
        self.chooser.bind(on_submit=self.update)

        popup.add_widget(self.chooser)
        imagelayout.add_widget(self.imagebox)
        imagelayout.add_widget(popupbutton)
        imagelayout.add_widget(launchbutton)
        resultlayout.add_widget(resultlabel)
        resultlayout.add_widget(ledimage)
        mainwindow.add_widget(imagelayout)
        mainwindow.add_widget(resultlayout)

        return mainwindow


if __name__ == '__main__':
    HackApp().run()
