from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.uix.label import *
from kivy.clock import Clock
from kivy.core.window import Window

w_width =  4*(Window.width + Window.height)

w_width = w_width / 6000
font = str(20 * w_width)
font = font + 'px'

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        my_text = 'Пройшло секунд:' + str(self.current)
        super().__init__(text = my_text,size_hint_y = None, height = '40px', font_size = font)
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = "Пройшло секунд:" + str(self.current)
        self.start()

    def start(self):
        Clock.schedule_interval(self.change,1)
    def change(self, dt):
        self.current += 1
        self.text = 'Пройшло секунд:' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False
