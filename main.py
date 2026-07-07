from manim import *
import numpy as np

class ManimCELogo(Scene):
    def construct(self):
        ellipsis1 = Ellipse(width=4, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10).move_to(LEFT)
        ellipsis2 = ellipsis1.copy().set_color(RED).move_to(RIGHT)
        boolean_ops = MarkupText("<u>Boolean Operations</u>", font_size=50).next_to(ellipsis1, UP, buff=1)
        ellipse_group = Group(boolean_ops, ellipsis1, ellipsis2).move_to(LEFT*3)
        self.play(FadeIn(ellipse_group))
        i = Intersection(ellipsis1, ellipsis2, fill_opacity=0.5, color=YELLOW)
        self.play(i.animate.scale(0.5).move_to(RIGHT*5 + UP*1.4))
        intersection_text = MarkupText("Intersection", font_size=25).next_to(i, UP, buff=1)
        self.play(FadeIn(intersection_text))



class SolarSystem(MovingCameraScene):
    def construct(self):

        self.add_sound("/home/nureyni/dev/al-khawarizmi/audio/game of throne.mp3")
        TIME_SIMULATION = 30

        self.camera.frame.set(width=35)
        camera_path = Ellipse(width=4, height=3)

        t = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda cam: cam.move_to(camera_path.point_from_proportion(t.get_value() % 1))
        )
        sun = Circle(radius=1, color=YELLOW, fill_opacity=1)
        self.add(sun)
        name_sun = Text("Sun", font_size=24).next_to(sun, DOWN)
        self.add(name_sun)
        orbit_mercury = Ellipse(width=5, height=4,color=GRAY)
        orbit_venus = Ellipse(width=7, height=6,color=GRAY)
        orbit_earth = Ellipse(width=9, height=8,color=GRAY)
        orbit_mars = Ellipse(width=11, height=10,color=GRAY)
        orbit_jupiter = Ellipse(width=13, height=12,color=GRAY)
        orbit_saturn = Ellipse(width=15, height=14,color=GRAY)
        orbit_uranus = Ellipse(width=17, height=16,color=GRAY)
        orbit_neptune = Ellipse(width=19, height=18,color=GRAY)

        
        self.add(orbit_mercury, orbit_venus, orbit_earth, orbit_mars, orbit_jupiter, orbit_saturn, orbit_uranus, orbit_neptune)
        mercury = Circle(radius=0.1, color=GRAY, fill_opacity=1)
        venus = Circle(radius=0.15, color=ORANGE, fill_opacity=1)
        earth = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        mars = Circle(radius=0.2, color=RED, fill_opacity=1)
        jupiter = Circle(radius=0.3, color=GOLD, fill_opacity=1)
        saturn = Circle(radius=0.35, color=WHITE, fill_opacity=1)
        uranus = Circle(radius=0.4, color=BLUE, fill_opacity=1)
        neptune = Circle(radius=0.45, color=BLUE, fill_opacity=1)
        ALPHA = PI / 4
        mercury_name = Text("Mercury", font_size=24).next_to(orbit_mercury.point_from_proportion(0), DOWN).rotate(ALPHA)
        venus_name = Text("Venus", font_size=24).next_to(orbit_venus.point_from_proportion(0), DOWN).rotate(ALPHA)
        earth_name = Text("Earth", font_size=24).next_to(orbit_earth.point_from_proportion(0), DOWN).rotate(ALPHA)
        mars_name = Text("Mars", font_size=24).next_to(orbit_mars.point_from_proportion(0), DOWN).rotate(ALPHA)  
        jupiter_name = Text("Jupiter", font_size=24).next_to(orbit_jupiter.point_from_proportion(0), DOWN).rotate(ALPHA)
        saturn_name = Text("Saturn", font_size=24).next_to(orbit_saturn.point_from_proportion(0), DOWN).rotate(ALPHA)
        uranus_name = Text("Uranus", font_size=24).next_to(orbit_uranus.point_from_proportion(0), DOWN).rotate(ALPHA)
        neptune_name = Text("Neptune", font_size=24).next_to(orbit_neptune.point_from_proportion(0), DOWN).rotate(ALPHA)
        self.add(mercury, venus,mercury_name, venus_name, earth, mars, earth_name, mars_name, jupiter, saturn, uranus, neptune, jupiter_name, saturn_name, uranus_name, neptune_name)

        # t = ValueTracker(0)
        
        # vitesse angulaire différente
        mercury_speed = 7.15
        venus_speed = 5.62
        earth_speed = 3.5
        mars_speed = 2.53 
        jupiter_speed = 1.5#0.3
        saturn_speed = 1.0
        uranus_speed = 0.5
        neptune_speed = 0.25
        planet = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
        planet_name = [mercury_name, venus_name, earth_name, mars_name, jupiter_name, saturn_name, uranus_name, neptune_name]
        speeds = [mercury_speed, venus_speed, earth_speed, mars_speed, jupiter_speed, saturn_speed, uranus_speed, neptune_speed]
        orbit_planet = [orbit_mercury, orbit_venus, orbit_earth, orbit_mars, orbit_jupiter, orbit_saturn, orbit_uranus, orbit_neptune]
        for i, p in enumerate(planet):
            p.add_updater(
                lambda m, i=i: m.move_to(
                    orbit_planet[i].point_from_proportion((t.get_value()*speeds[i]) % 1)
                )
            )
            planet_name[i].add_updater(
                lambda m, i=i: m.next_to(
                    orbit_planet[i].point_from_proportion((t.get_value()*speeds[i]) % 1), DOWN
                )
            )
        self.play(t.animate.set_value(1), run_time=TIME_SIMULATION, rate_func=linear)


import numpy as np
from manim import *

class BaseScene(MovingCameraScene):
    def setup(self):
        super().setup()

        # --- Logo, coin inférieur gauche ---
        logo = ImageMobject(
            "/home/nureyni/dev/al-khawarizmi/media/images/logo/LogoAlKhawarizmi_ManimCE_v0.19.0.png"
        ).scale(0.3)
        logo.set_opacity(0.85)
        self._pin_to_corner(logo, DL, buff=0.3)
        self.add(logo)

        self.hud_logo = logo  # au cas où tu veux y accéder plus tard

    def _pin_to_corner(self, mobject, corner, buff=0.3):
        """
        Ajoute un updater qui garde `mobject` collé au coin `corner`
        du cadre de la caméra (self.camera.frame), même si celle-ci
        bouge ou zoome.
        """
        def updater(m):
            frame = self.camera.frame
            target = frame.get_corner(corner)
            dx = -np.sign(corner[0]) * (m.width / 2 + buff)
            dy = -np.sign(corner[1]) * (m.height / 2 + buff)
            m.move_to(target + np.array([dx, dy, 0]))
        mobject.add_updater(updater)


class ComplexPlan(BaseScene):
    def construct(self):
        self.add_sound("/home/nureyni/dev/al-khawarizmi/audio/chunks/chunk_004.mp3")
        TIME_SIMULATION = 20
        self.camera.frame.set(width=35)

        camera_path = Ellipse(width=4, height=3)
        t = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda cam: cam.move_to(camera_path.point_from_proportion(t.get_value() % 1))
        )

        axes = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=20,
            y_length=20,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 24,
            },
        )
        labels = axes.get_axis_labels(x_label="\\mathrm{Re}", y_label="\\mathrm{Im}")
        origin_point = Dot(axes.c2p(0, 0), color=GREEN)

        # --- Formules, coin supérieur gauche, pinnées au cadre ---
        complex_numbers_notation = MathTex("z = x + iy", font_size=36)
        transformation_text = MathTex("z \\mapsto z e^{i\\theta}", font_size=36)

        formulas = VGroup(complex_numbers_notation, transformation_text).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        self._pin_to_corner(formulas, UL, buff=0.5)
        self.add(formulas)

        self.play(Create(axes), Write(labels), FadeIn(origin_point))

        # --- Génération de N nombres complexes ---
        N = 5_000
        np.random.seed(42)
        real_parts = np.random.uniform(-8, 8, N)
        imag_parts = np.random.uniform(-8, 8, N)
        z0 = real_parts + 1j * imag_parts

        moduli = np.abs(z0)
        moduli_norm = moduli / moduli.max()
        colors = [interpolate_color(BLUE, RED, m) for m in moduli_norm]

        dots = VGroup(*[
            Dot(axes.c2p(z.real, z.imag), radius=0.05, color=colors[i])
            for i, z in enumerate(z0)
        ])

        def update_dots(mob):
            theta = t.get_value() * 2 * PI
            zt = z0 * np.exp(1j * theta)
            for dot, z in zip(mob, zt):
                dot.move_to(axes.c2p(z.real, z.imag))

        dots.add_updater(update_dots)
        self.add(dots)

        self.play(t.animate.set_value(1), run_time=TIME_SIMULATION, rate_func=linear)