from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class TestApp(App):
    def build(self):
        grid_layout = GridLayout(cols=4)
        grid_layout.add_widget(Button(text='1'))
        grid_layout.add_widget(Button(text='2'))
        grid_layout.add_widget(Button(text='3'))
        grid_layout.add_widget(Button(text='4'))
        grid_layout.add_widget(Button(text='5'))
        grid_layout.add_widget(Button(text='6'))
        grid_layout.add_widget(Button(text='7'))
        grid_layout.add_widget(Button(text='8'))
        grid_layout.add_widget(Button(text='9'))
        grid_layout.add_widget(Button(text='10'))
        grid_layout.add_widget(Button(text='11'))
        grid_layout.add_widget(Button(text='12'))
        grid_layout.add_widget(Button(text='13'))
        grid_layout.add_widget(Button(text='14'))
        grid_layout.add_widget(Button(text='15'))
        grid_layout.add_widget(Button(text='16'))
        return grid_layout


TestApp().run()