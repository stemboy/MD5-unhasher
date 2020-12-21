from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color


class ConfigLayout(BoxLayout):
    o = NumericProperty(0)

    def on_enter(self):
        self.o = 0
        a = Animation(o=1, duration=1)
        a.bind(on_progress=self.draw_bg)
        a.start(self)

        self.bind(pos=self.draw_bg, size=self.draw_bg)

    def draw_bg(self, *args):
        n = 0
        colors = (0.3, 0.3, 0.3), (0.5, 0.5, 0.5)

        with self.canvas.before:
            self.canvas.before.clear()

            for child in self.children:
                if child.__class__.__name__ != "Widget":

                    Color(rgb=colors[n], a=self.o)
                    Rectangle(pos=child.pos, size=(Window.width, child.height))

                n = (n + 1) % 2
