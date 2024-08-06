from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Line, Ellipse, Color, Rectangle
from kivy.core.text import Label as CoreLabel
from math import cos, sin, radians
from datetime import datetime

class AnalogClock(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)

    def update_time(self, dt):
        self.canvas.clear()
        with self.canvas:
            self.draw_clock_face()
            self.draw_hands()

    def draw_clock_face(self):
        Color(1, 1, 1)
        self.center_x, self.center_y = self.center
        self.radius = min(self.center_x, self.center_y) - 20
        Ellipse(pos=(self.center_x - self.radius, self.center_y - self.radius), size=(self.radius * 2, self.radius * 2))

        # Draw hour markers and numbers
        for hour in range(1, 13):
            angle = radians((hour - 3) * 30)
            x_start = self.center_x + self.radius * 0.85 * cos(angle)
            y_start = self.center_y + self.radius * 0.85 * sin(angle)
            x_end = self.center_x + self.radius * 0.95 * cos(angle)
            y_end = self.center_y + self.radius * 0.95 * sin(angle)
            Line(points=[x_start, y_start, x_end, y_end], width=2)

            # Draw numbers
            label = CoreLabel(text=str(hour), font_size=24, color=(0, 0, 0, 1))
            label.refresh()
            text = label.texture
            text_width, text_height = text.size
            x_number = self.center_x + (self.radius - 50) * cos(angle) - text_width / 2
            y_number = self.center_y + (self.radius - 50) * sin(angle) - text_height / 2
            Rectangle(texture=text, pos=(x_number, y_number), size=text.size)

    def draw_hands(self):
        now = datetime.now()

        # Draw hour hand
        Color(0, 0, 1)
        self.draw_hand((now.hour % 12) * 30 + (now.minute / 2), 0.5, 4)

        # Draw minute hand
        Color(0, 1, 0)
        self.draw_hand(now.minute * 6, 0.7, 2)

        # Draw second hand
        Color(1, 0, 0)
        self.draw_hand(now.second * 6, 0.9, 1)

    def draw_hand(self, angle_degrees, length_ratio, width):
        angle = radians(angle_degrees - 90)
        x_end = self.center_x + self.radius * length_ratio * cos(angle)
        y_end = self.center_y + self.radius * length_ratio * sin(angle)
        Line(points=[self.center_x, self.center_y, x_end, y_end], width=width)

class AnalogClockApp(App):
    def build(self):
        return AnalogClock()

if __name__ == '__main__':
    AnalogClockApp().run()
