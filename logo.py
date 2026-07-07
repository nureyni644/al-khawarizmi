from manim import *
import numpy as np

GOLD_LIGHT = "#f4d878"
GOLD_MID = "#caa136"
GOLD_DARK = "#8a6a1f"
BG_BLACK = "#0b0b0c"

# manim -qh --format=png logo.py LogoAlKhawarizmi -s

class LogoAlKhawarizmi(Scene):
    def construct(self):
        self.camera.background_color = BG_BLACK

        # --- Cercles concentriques ---
        outer_circle = Circle(radius=2.2, color=GOLD_MID, stroke_width=3)
        inner_circle = Circle(radius=1.9, color=GOLD_MID, stroke_width=1.5)

        # --- Étoile à 8 branches (superposition de 2 carrés tournés à 45°) ---
        square1 = Square(side_length=2.6, color=GOLD_MID, stroke_width=3)
        square2 = square1.copy().rotate(PI / 4)
        star_outline = VGroup(square1, square2)

        # --- Étoile pleine (remplissage doré) ---
        star_fill = self.make_eight_point_star(outer_radius=1.6, inner_radius=0.75)
        star_fill.set_fill(GOLD_MID, opacity=1)
        star_fill.set_stroke(GOLD_LIGHT, width=1)

        # --- Cercle central noir (fond pour le monogramme) ---
        center_circle = Circle(radius=0.85, color=GOLD_LIGHT, stroke_width=2)
        center_circle.set_fill(BG_BLACK, opacity=1)

        # --- Monogramme AK ---
        monogram = Text("AK", font="Georgia", weight=BOLD, color=GOLD_LIGHT)
        monogram.scale(1.1)
        monogram.move_to(center_circle.get_center())

        logo = VGroup(
            outer_circle, inner_circle, star_outline,
            star_fill, center_circle, monogram
        )
        logo.move_to(ORIGIN)

        # --- Nom en dessous ---
        name = Text("al-khawarizmi", font="Georgia", color=GOLD_MID)
        name.scale(0.5)
        name.next_to(logo, DOWN, buff=0.4)

        # --- Animation d'apparition ---
        self.play(Create(outer_circle), Create(inner_circle), run_time=1.2)
        self.play(Create(star_outline), run_time=1.2)
        self.play(DrawBorderThenFill(star_fill), run_time=1.5)
        self.play(Create(center_circle), run_time=0.8)
        self.play(Write(monogram), run_time=1)
        self.play(FadeIn(name, shift=UP * 0.2), run_time=1)
        self.wait(1)

    def make_eight_point_star(self, outer_radius, inner_radius):
        """Génère une étoile à 8 branches comme Polygon."""
        n_points = 8
        vertices = []
        for i in range(2 * n_points):
            angle = i * PI / n_points
            r = outer_radius if i % 2 == 0 else inner_radius
            vertices.append([r * np.cos(angle), r * np.sin(angle), 0])
        return Polygon(*vertices)