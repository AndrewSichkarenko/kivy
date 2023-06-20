from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.uix.label import *
from kivy.clock import Clock

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        my_text = 'Пройшло секунд:' + str(self.current)
        self.height = '50px'
        super().__init__(text = my_text)
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
