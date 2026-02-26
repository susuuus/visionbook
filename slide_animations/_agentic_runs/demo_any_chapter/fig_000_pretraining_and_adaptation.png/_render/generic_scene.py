
from manim import *

class GenericFigure(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        fig = ImageMobject(r"""/Users/su/Documents/su/visionbook/figures/transfer_learning/pretraining_and_adaptation.png""").scale_to_fit_width(11)
        txt = Text("Transfer learning consists of two phases: first we pretrain a model on one task and then we adapt that model to perform a new task.", color=BLACK, font_size=28).to_edge(DOWN)
        self.play(FadeIn(fig), run_time=0.6)
        if "Transfer learning consists of two phases: first we pretrain a model on one task and then we adapt that model to perform a new task.":
            self.play(FadeIn(txt), run_time=0.4)
        self.wait(2.0)
        self.play(FadeOut(Group(fig, txt)), run_time=0.6)
