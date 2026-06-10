from manim import *


class Scene1Intro(Scene):
    def construct(self):
        title = Text("Scene 1: Intro")
        self.play(Write(title))
        self.wait(1)
