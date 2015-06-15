from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from os.path import join, dirname

def playsound(instance):

    filename = join(dirname(__file__), 'sounds/{0}.wav'.format(instance.id))
    sound = SoundLoader.load(filename)
    if sound:
        sound.play()


def generate_buttons(layout):
    # loop 16 times ( from 1 to 17 )
    # counter will hold the current loop index
    # counter will be 1 the first time, 2 the second time
    # when counter reaches 17 it will stop and NOT perform
    # the loop a 17th time
    for counter in range(1, 17):
        new_button = Button(id="{0}".format(counter))
        new_button.bind(on_press=playsound)
        layout.add_widget(new_button)

class TestApp(App):

    # 'build(self)' is a function that the Kivy library expects any
    # object that inherits from App to implement. It is expected to
    # create and return a layout object that contains the instructions
    # for building the user interface
    def build(self):

        main_layout = BoxLayout(orientation='vertical', padding=20)  # create a main layout object called "main_layout"
        header_layout = StackLayout()  # create a StackLayout called header_layout

        # add a size_hint attribute to the header_layout, this will tell the parent layout which
        # proportions it should use when sizing the header_layout with respect to it's neighbors
        header_layout.size_hint = (1, .2)

        title = Label(text='KIVY MPC')   # create a Label called title with the text "KIVY MPC"
        header_layout.add_widget(title)  # add title to header_layout
        main_layout.add_widget(header_layout)  # add the header_layout to the main_layout

        grid_layout = GridLayout(cols=4)  # create a grid layout to contain the drum pads

        generate_buttons(grid_layout)  # pass the grid_layout to the generate_buttons function in order to create the 16 buttons

        main_layout.add_widget(grid_layout)  # add the grid layout

        return main_layout  # return the main_layout to the kivy environment

TestApp().run()  # run the test app