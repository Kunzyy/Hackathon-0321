from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

print('Hello world !')


class LoginScreen(GridLayout):
    def __init__(self, **var_args):
        super(LoginScreen, self).__init__(**var_args)


class MyApp(App):
    def build(self):
        # return a LoginScreen() as a root widget
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()