from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime

class ClockApp(App):
    def build(self):
        self.label = Label(font_size='70sp')
        Clock.schedule_interval(self.update_time, 1)
        return self.label

    def update_time(self, *args):
        self.label.text = datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    ClockApp().run()
