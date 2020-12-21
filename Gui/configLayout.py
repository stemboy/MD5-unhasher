from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color


class ConfigLayout(BoxLayout):
    def on_kv_post(self, base_widget):
        self.draw_bg()

        Window.bind(size=self.draw_bg)

    def draw_bg(self, *args):
        n = 0
        colors = (0.3, 0.3, 0.3), (0.5, 0.5, 0.5)

        with self.canvas.before:
            self.canvas.before.clear()

            for child in self.children:
                if child.__class__.__name__ != "Widget":

                    Color(rgb=colors[n])
                    Rectangle(pos=child.pos, size=child.size)

                n = (n + 1) % 2
