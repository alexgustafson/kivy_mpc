from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20)
        header_layout = StackLayout()
        header_layout.size_hint = (1, .2)

        title = Label(text='KIVY MPC')
        header_layout.add_widget(title)
        main_layout.add_widget(header_layout)

        grid_layout = GridLayout(cols=4)
        grid_layout.add_widget(Button(id='1'))
        grid_layout.add_widget(Button(id='2'))
        grid_layout.add_widget(Button(id='3'))
        grid_layout.add_widget(Button(id='4'))
        grid_layout.add_widget(Button(id='5'))
        grid_layout.add_widget(Button(id='6'))
        grid_layout.add_widget(Button(id='7'))
        grid_layout.add_widget(Button(id='8'))
        grid_layout.add_widget(Button(id='9'))
        grid_layout.add_widget(Button(id='10'))
        grid_layout.add_widget(Button(id='11'))
        grid_layout.add_widget(Button(id='12'))
        grid_layout.add_widget(Button(id='13'))
        grid_layout.add_widget(Button(id='14'))
        grid_layout.add_widget(Button(id='15'))
        grid_layout.add_widget(Button(id='16'))

        main_layout.add_widget(grid_layout)

        return main_layout


TestApp().run()