from manim import *


class Scene3Text(Scene):
    def construct(self):
        title = Text("Scene 3: Text")
        self.play(Write(title))
        self.wait(1)
