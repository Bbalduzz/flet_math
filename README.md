<p align="center">
  <img width="30%" align="center" src="https://github.com/user-attachments/assets/03e0bb8f-aead-4dbb-9f3e-a3d18f866514" alt="logo">
</p>
<p align="center">
  A flet extension to render LaTex formulas
</p>

<p align="center">
  <img width="40%" align="center" src="https://github.com/user-attachments/assets/b8ce9b51-c385-422c-8c65-08673158374c" alt="logo">
</p>


### How to use it
This works only when building applicatons. 
1. in your `pyproject.toml` add it in your dependecies
  ```toml
  dependencies = [
      "flet_math @ https://github.com/Bbalduzz/flet_math.git"
  ]
  ```
2. then build witn `flet build`
  ```cmd
  flet build <target> -v
  ```
#### usage
  ```python
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
     )
    page.update()


ft.app(target=main)
  ```
