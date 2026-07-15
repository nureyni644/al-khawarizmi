from manim import *  # ou "from manim import *" selon ta lib (ManimCE / ManimGL)
import numpy as np


class BaseScene(MovingCameraScene):
    def setup(self):
        super().setup()

        # --- Logo, coin inférieur gauche ---
        logo = ImageMobject(
            "/home/nureyni/dev/al-khawarizmi/media/images/logo/LogoAlKhawarizmi_ManimCE_v0.19.0.png"
        ).scale(0.3)
        logo.set_opacity(0.85)
        self._pin_to_corner(logo, DR, buff=0.3)
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

class Translation(BaseScene):
    def construct(self):
        self.add_sound("/home/nureyni/dev/al-khawarizmi/audio/chunks/chunk_005.mp3")

        TIME_SIMULATION = 10
        self.camera.frame.set(width=35)

        cam_path = Ellipse(width=4, height=3)
        t = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda cam: cam.move_to(cam_path.point_from_proportion(t.get_value() % 3))
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
        self.add(axes)

        # ---------------------------------------------------------
        # 1) Definition des nombres complexes
        # ---------------------------------------------------------
        z = complex(-4, 3)      # affixe du point M
        b = complex(6, 4)      # affixe du vecteur de translation
        z_prime = z + b        # affixe de M' = image de M par la translation

        def to_point(c):
            return axes.c2p(c.real, c.imag)
        
        # ---------------------------------------------------------
        # 2) Point M et son affixe
        # ---------------------------------------------------------
        M = Dot(to_point(z), color=YELLOW, radius=0.12)
        O_M_Vector = Arrow(
            start=to_point(0),
            end=to_point(z),
            buff=0,
            color=YELLOW,
            stroke_width=6,
        )
        M_label = MathTex("M").next_to(M, DOWN, buff=0.3)
        z_label = MathTex(f"z = {z}").next_to(M, UP, buff=0.3)
        z_label.set_color(YELLOW)
        
        # self.play(FadeIn(M_label,scale=0.5))
        self.play(Group(O_M_Vector, z_label).animate.set_run_time(1.5))
        # self.play(Write(z_label))
        self.wait(1)

        # ---------------------------------------------------------
        # 3) Titre / formule generale de la translation
        # ---------------------------------------------------------
        formule = MathTex(r"z' = z + b").to_corner(UL, buff=1)
        formule.scale(2.5)
        # self.add_fixed_in_frame_mobjects(formule) if hasattr(self, "add_fixed_in_frame_mobjects") else self.add(formule)
        # self.play(Write(formule))
        self.wait(1)

        # ---------------------------------------------------------
        # 4) Vecteur de translation b, trace depuis M
        # ---------------------------------------------------------
        # vecteur_b = Arrow(
        #     start=to_point(z),
        #     end=to_point(z_prime),
        #     buff=0,
        #     color=GREEN,
        #     stroke_width=6,
        # )
        B = Dot(to_point(b), color=GREEN, radius=0.12)
        O_B_Vector = Arrow(
            start=to_point(0),
            end=to_point(b),
            buff=0,
            color=GREEN,
            stroke_width=6,
        )
        # self.play(FadeIn(B, scale=0.5))
        B_label = MathTex(f"B").set_color(WHITE).next_to(B, UP, buff=0.3)
        b_label = MathTex(f"b = {b}").set_color(GREEN).next_to(B, DOWN, buff=0.3)
        self.play(Group(O_B_Vector, B_label).animate.set_run_time(1.5))
        # b_label.next_to(vecteur_b.get_center(), UP, buff=0.25)

        # self.play(GrowArrow(vecteur_b))
        # self.play(Write(b_label))
        self.wait(1)

        # ---------------------------------------------------------
        # 5) Apparition du point M' (image de M)
        # ---------------------------------------------------------
        M_prime = Dot(to_point(z_prime), color=RED, radius=0.12)
        O_M_prime_Vector = Arrow(
            start=to_point(0),
            end=to_point(z_prime),
            buff=0,
            color=RED,
            stroke_width=6,
        )
        M_prime_label = MathTex("M'").next_to(M_prime, DOWN, buff=0.3)
        
        formule_label_group = VGroup(formule, z_label, b_label).to_corner(UL, buff=1)
        self.play(Write(formule_label_group))   
        

        self.play(
            TransformFromCopy(M, M_prime),
            run_time=1.5,
        )
        self.play(
            TransformFromCopy(O_M_Vector, O_M_prime_Vector),
            run_time=1.5,
        )
        # self.play(FadeIn(M_prime_label, scale=0.5))
        
        t.set_value(0)
        self.play(t.animate.set_value(TIME_SIMULATION), run_time=TIME_SIMULATION, rate_func=linear)
        self.wait(2)
