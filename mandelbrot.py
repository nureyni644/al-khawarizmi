"""
Fonction de récurrence pour la suite de Mandelbrot : u_{n+1} = u_n^2 + c
"""


def mandelbrot(u_n: complex, c: complex) -> complex:
    return u_n ** 2 + c


import numpy as np
import matplotlib.cm as cm
from manim import *


def smooth_mandelbrot(center: complex, zoom: float, resolution: int, max_iter: int) -> np.ndarray:
    """
    Calcule une image RGB (uint8) de l'ensemble de Mandelbrot avec un comptage
    d'itérations lissé (continuous escape-time), ce qui évite l'effet de
    bandes de couleur brutales et donne un dégradé bien plus doux.
    """
    scale = 3.0 / zoom
    x = np.linspace(center.real - scale / 2, center.real + scale / 2, resolution)
    y = np.linspace(center.imag - scale / 2, center.imag + scale / 2, resolution)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    smooth_iter = np.zeros(C.shape, dtype=float)
    escaped = np.zeros(C.shape, dtype=bool)

    for n in range(max_iter):
        active = ~escaped
        Z[active] = Z[active] ** 2 + C[active]
        newly_escaped = active & (np.abs(Z) > 2)
        with np.errstate(invalid="ignore", divide="ignore"):
            smooth_iter[newly_escaped] = (
                n + 1 - np.log(np.log(np.abs(Z[newly_escaped]))) / np.log(2)
            )
        escaped |= newly_escaped

    smooth_iter[~escaped] = max_iter  # points restés dans l'ensemble

    # On répète le dégradé de couleurs plusieurs fois : ça fait ressortir
    # les nouvelles structures fractales révélées à chaque niveau de zoom.
    cycles = 4
    normalized = (smooth_iter / max_iter * cycles) % 1.0
    colored = cm.turbo(normalized)
    rgb_array = (colored[:, :, :3] * 255).astype(np.uint8)
    rgb_array[~escaped] = [5, 5, 15]  # intérieur de l'ensemble : quasi noir
    return rgb_array


def max_iter_for_zoom(zoom: float) -> int:
    """Plus on zoome, plus il faut d'itérations pour révéler le détail."""
    return int(80 + 40 * np.log2(zoom + 1))


class Mandelbrot(ThreeDScene):
    def construct(self):
        # Vue quasi frontale : un fort tilt 3D déforme surtout une image plate
        self.set_camera_orientation(phi=15 * DEGREES, theta=-90 * DEGREES)

        center = complex(-0.7463, 0.1102)  # "vallée des hippocampes"
        resolution = 350  # montez à 500+ pour le rendu final en qualité haute

        zoom_tracker = ValueTracker(1)

        def get_frame():
            zoom = zoom_tracker.get_value()
            arr = smooth_mandelbrot(center, zoom, resolution, max_iter_for_zoom(zoom))
            img = ImageMobject(arr)
            img.height = 6
            img.move_to(ORIGIN)
            return img

        image = always_redraw(get_frame)
        self.add(image)

        self.begin_ambient_camera_rotation(rate=0.03)  # rotation à peine perceptible
        self.play(zoom_tracker.animate.set_value(3000), run_time=20, rate_func=linear)
        self.stop_ambient_camera_rotation()

        self.wait(2)
        self.play(FadeOut(image))
        self.wait(1)
