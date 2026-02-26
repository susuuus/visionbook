
from manim import *

class GenericFigure(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        fig = ImageMobject(r"""figures/homography/IMG_7801_crop.jpg""").scale_to_fit_width(11)
        txt = Text("", color=BLACK, font_size=28).to_edge(DOWN)
        self.play(FadeIn(fig), run_time=0.6)
        if "":
            self.play(FadeIn(txt), run_time=0.4)
        self.wait(2.0)
        self.play(FadeOut(Group(fig, txt)), run_time=0.6)
