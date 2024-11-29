from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9

class Trig_Circ(Scene):
    def construct(self):
        range = [-1.4, 1.4, 1]
        r = 2.5
        length = r * (range[1] - range[0])
        ax = Axes(x_range=range, x_length=length, y_range=range, y_length=length, axis_config={"include_numbers": True})
        c = Circle(radius=r, color=rgb_to_color([0.0, 0.0, 1.0]))

        ax.x_axis.numbers[0].shift(r*(LEFT*0.2+UP*0.1)/2.5)
        ax.x_axis.numbers[1].shift(r*(RIGHT*0.2+UP*0.1)/2.5)
        ax.y_axis.numbers[0].shift(r*(DOWN*0.25+RIGHT*0.1)/2.5)
        ax.y_axis.numbers[1].shift(r*(UP*0.25+RIGHT*0.1)/2.5)

        self.play(Create(ax), Create(c), run_time=2)

        k = ValueTracker(0)

        l = always_redraw(lambda: Line(start=c.get_center(), end=c.point_at_angle(k.get_value()), color=YELLOW))
        d = always_redraw(lambda: Dot(c.point_at_angle(k.get_value()), color=rgb_to_color([1.0, 0.0, 0.0])))

        self.play(Create(l), Create(d))
        self.wait(0.5)

        dl1 = always_redraw(lambda: DashedLine(start=[r*np.cos(k.get_value()), 0, 0], end=c.point_at_angle(k.get_value()), color=WHITE))
        dl2 = always_redraw(lambda: DashedLine(start=[0, r*np.sin(k.get_value()), 0], end=c.point_at_angle(k.get_value()), color=WHITE))
        arc = always_redraw(lambda: Arc(radius=0.5, start_angle=0, angle=k.get_value(), color=rgb_to_color([0.0, 1.0, 0.0]), stroke_width=2))
        angle = always_redraw(lambda: MathTex(r"\theta").scale(0.75).next_to(arc.point_from_proportion(0.5), direction=arc.point_from_proportion(0.5) - ORIGIN, buff=0.2).shift(DOWN*0.1).set_color(rgb_to_color([0.0, 1.0, 0.0])))
        lx = always_redraw(lambda: Line(start=ORIGIN, end=[r*np.cos(k.get_value()), 0, 0], color=BLACK))
        ly = always_redraw(lambda: Line(start=ORIGIN, end=[0, r*np.sin(k.get_value()), 0], color=BLACK))
        bx = always_redraw(lambda: Brace(lx, direction=DOWN))
        by = always_redraw(lambda: Brace(ly, direction=LEFT))
        bx_text = always_redraw(lambda: bx.get_tex(r"\cos \theta").scale(0.75))
        by_text = always_redraw(lambda: by.get_tex(r"\sin \theta").scale(0.75))

        self.add(dl1, dl2, arc, angle,lx, ly, bx, by, bx_text, by_text)
        
        self.bring_to_front(d)
        self.bring_to_back(lx, ly)

        self.play(k.animate.set_value(9*PI/32), run_time=2, rate_func=smooth)
        self.wait(0.5)

        dl3 = DashedLine(start=d.get_center(), end=[r/np.tan(k.get_value()), r, 0], color=YELLOW)
        lc = Line(start=[0, r, 0], end=dl3.get_end())
        bcot = Brace(lc, direction=UP)
        bcot_text = bcot.get_tex(r"\cot \theta").scale(0.75)
        dlcot = DashedLine(start=[r*range[0], r, 0], end=[r*range[1], r, 0], color=WHITE)

        dl4 = DashedLine(start=dl3.get_end(), end=[r, r*np.tan(k.get_value()), 0], color=YELLOW)
        lt = Line(start=[r, 0, 0], end=dl4.get_end())
        btan = Brace(lt, direction=RIGHT)
        btan_text = btan.get_tex(r"\tan \theta").scale(0.75)
        dltan = DashedLine(start=[r, r*range[0], 0], end=[r, r*range[1], 0], color=WHITE)

        dc = Dot(point=dl3.get_end(), color=rgb_to_color([1.0, 0.0, 0.0]))        
        dt = Dot(point=dl4.get_end(), color=rgb_to_color([1.0, 0.0, 0.0]))
        
        self.play(Create(dlcot))

        self.play(Create(VGroup(dl3, dc), run_time=1.5))
        self.play(Write(VGroup(bcot, bcot_text), run_time=2))

        self.play(Create(dltan))

        self.play(Create(VGroup(dl4, dt), run_time=1.5))
        self.play(Write(VGroup(btan, btan_text), run_time=2))
        self.wait()
        

        lsec = Line(start=ORIGIN, end=dl4.get_end())
        direction=DOWN*np.cos(k.get_value()) + RIGHT*np.sin(k.get_value())
        bsec = Brace(lsec, direction=direction)
        bsec_text = bsec.get_tex(r"\sec \theta").scale(0.65).shift(-direction * 0.85 + DOWN*0.2).rotate(k.get_value())
        
        lcosec = Line(start=ORIGIN, end=dl3.get_end())
        direction = UP*np.cos(k.get_value()) + LEFT*np.sin(k.get_value())
        bcosec = Brace(lcosec, direction=direction)
        bcosec_text = bcosec.get_tex(r"\text{cosec} \, \theta").scale(0.65).shift(-direction * 0.95 + UP*0.3).rotate(k.get_value())

        self.play(Write(VGroup(bsec, bsec_text, bcosec, bcosec_text)), FadeOut(VGroup(dl1, dl2, bx, by, bx_text, by_text)), run_time=4)
        self.wait(2)
