import manim as mn
from manim import Axes

class SineCosineGraph(mn.Scene):
    def construct(self):
       
        axes = Axes(
            x_range=[-2*mn.PI, 2 * mn.PI],
            y_range=[-1, 1],
            axis_config={"color": mn.GRAY},
        )
        carre = mn.Square(side_length=3, color=mn.YELLOW).shift(mn.LEFT * 5)
        f_x = mn.Tex("sin(x)")
        f_y = mn.Tex("cos(x)")
        group_text = mn.VGroup(f_x, f_y,carre).arrange(mn.DOWN) #.to_corner(mn.UP + mn.RIGHT)
        group_text.move_to(carre.get_center())
        legend_group = mn.VGroup(group_text,carre)
        sin_graph = axes.plot(mn.np.sin, color=mn.BLUE)
        cos_graph = axes.plot(mn.np.cos, color=mn.RED)

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        
        # self.play(mn.Create(axes), mn.Write(labels))
        self.play(mn.Write(group_text ))
        self.play(mn.Create(carre))
        # self.play(mn.Create(sin_graph), mn.Create(cos_graph))

        self.wait(4)
