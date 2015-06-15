from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from os.path import join, dirname
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

import datetime, threading, time #

seq_should_run = False


class SequencerTimer(object): # http://stackoverflow.com/questions/8418067/python-what-is-the-proper-way-to-pass-arguments-to-threading-thread-instance

    def __init__(self, state, tempo):
        self.state = state
        self.tempo = tempo
        self.set_tickinterval()

    def set_state(self, state):
        self.state = state

    def set_tempo(self, tempo):
        self.tempo = tempo
        self.set_tickinterval()

    def set_tickinterval(self):
        self.tickinterval = 60 / self.tempo

    def toggleState(self):
        if self.state != "playing":
            self.state = "playing"
            timerThread = threading.Thread(target=self.run)
            timerThread.daemon = True
            timerThread.start()
        else:
            self.state = "stopped"

    def run(self):
        next_tick = time.time()
        while self.state == "playing":
            print datetime.datetime.now()
            next_tick = next_tick +  0.01
            time.sleep(60 / self.tempo)

seqTimer = SequencerTimer("stopped", 120)

def tick():
    while seq_should_run:
        print datetime.datetime.now()
        time.sleep(60 / self.tempo)

#timerThread = threading.Thread(target=tick)
#timerThread.daemon = True


def ticker(instance):
    seqTimer.toggleState()



filename = join(dirname(__file__), 'sounds/1.wav')
sound = SoundLoader.load(filename)
tempo = 120

def playsound(dt):
    if sound:
        sound.play()


def start_sequnce(instance):
    Clock.schedule_interval(playsound, tempo / 60)

def tempo_change(instance, event):
    tempo = instance.value
    Clock.schedule_interval(playsound, tempo / 60)


class Seq(App):

    def build(self):
        main_layout = BoxLayout()
        main_layout.add_widget(Button(on_press=ticker, tag="play"))
        main_layout.add_widget(Slider(min=50, max=200, value=120, on_touch_move=tempo_change))
        return main_layout


if __name__ == '__main__':
    Seq().run()




