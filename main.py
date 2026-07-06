from manim import *

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

from manim import *
import numpy as np

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
