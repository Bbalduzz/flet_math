# examples/flet_math_example/src/main.py
import flet as ft
from flet_math import FletMath


def main(page: ft.Page):
    page.title = "Flet Math Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Text("Flet Math - LaTeX Rendering", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        ft.Text("Basic equation:", size=20),
        FletMath(
            tex=r"E = mc^2",
            text_size=24,
        ),
        
        ft.Text("Integrals:", size=20),
        FletMath(
            tex=r"\int_{a}^{b} f(x) \, dx = F(b) - F(a)",
            text_size=24,
            text_color=ft.colors.GREEN_800,
        ),
        
        ft.Text("Derivatives:", size=20),
        FletMath(
            tex=r"\frac{d}{dx}[x^n] = nx^{n-1}",
            text_size=24,
            text_color=ft.colors.BLUE_800,
        ),
        
        ft.Text("Limits:", size=20),
        FletMath(
            tex=r"\lim_{x \to \infty} \frac{1}{x} = 0",
            text_size=24,
            text_color=ft.colors.PURPLE_800,
        ),
        
        ft.Text("Summation:", size=20),
        FletMath(
            tex=r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}",
            text_size=24,
            text_color=ft.colors.ORANGE_800,
        ),
        
        ft.Text("Matrix:", size=20),
        FletMath(
            tex=r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            text_size=24,
            text_color=ft.colors.RED_800,
        ),
        
        ft.Text("Quadratic Formula:", size=20),
        FletMath(
            tex=r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            text_size=24,
            text_color=ft.colors.TEAL_800,
        ),
        
        ft.Text("Taylor Series:", size=20),
        FletMath(
            tex=r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n",
            text_size=24,
            text_color=ft.colors.BROWN_800,
        ),

        FletMath(
            tex=r"""
\begin{aligned} 
\lim_{x \to 0} \frac{1-\cos x}{x^2} &= \lim_{x \to 0} \frac{(1-\cos x)(1+\cos x)}{x^2(1+\cos x)} \\
&= \lim_{x \to 0} \frac{1-\cos^2 x}{x^2(1+\cos x)} \\
&= \lim_{x \to 0} \frac{\operatorname{sen}^2 x}{x^2(1+\cos x)} \\
&= \lim_{x \to 0} \frac{\operatorname{sen}^2 x}{x^2} \frac{1}{(1+\cos x)} \\
&= \lim_{x \to 0} \frac{\operatorname{sen}^2 x}{x^2} \cdot \lim_{x \to 0} \frac{1}{(1+\cos x)} \\
&= 1 \left(\frac{1}{2}\right) \\
&= \frac{1}{2}
\end{aligned}
            """,
            text_size=24,
        )
    )

    page.update()


ft.app(target=main)