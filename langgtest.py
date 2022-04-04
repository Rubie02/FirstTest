from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from matplotlib.pyplot import show

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Widgetss(Widget):
    def btn(self):
        show_popup()
        
class P(FloatLayout):
    pass
kv = Builder.load_file("popup.kv")
class MyMainApp(App):
    def build(self):
        return kv
 
def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(300, 300))
    popupWindow.open()

if __name__ == "__main__":
    MyMainApp().run()