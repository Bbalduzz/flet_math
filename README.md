<p align="center">
  <img width="30%" align="center" src="https://github.com/user-attachments/assets/03e0bb8f-aead-4dbb-9f3e-a3d18f866514" alt="logo">
</p>
<p align="center">
  A flet extension to render LaTex formulas
</p>

<div align="center">
  <table>
    <tr>
      <td width="30%">
        <img width="100%" src="https://github.com/user-attachments/assets/b8ce9b51-c385-422c-8c65-08673158374c" alt="logo">
      </td>
      <td width="70%">
        <video width="100%" src="https://github.com/user-attachments/assets/5ab84e51-4f43-4083-ba0a-2fd5989bfb2f">
      </td>
    </tr>
  </table>
</div>

## Installation
available in pypi:
```cmd
pip install flet_math
```

1. Add the dependency to your `pyproject.toml`:
```toml
dependencies = [
    "flet_math" # or flet_math @ git+https://github.com/Bbalduzz/flet_math.git
]
```

2. Build with `flet build`:
```cmd
flet build <target> -v
```

## Basic Usage

Here's a simple example of rendering a mathematical equation:

```python
import flet as ft
from flet_math import Math

def main(page: ft.Page):
    page.title = "Flet Math Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Text("Flet Math - LaTeX Rendering", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        ft.Text("Basic equation:", size=20),
        Math(
            tex=r"E = mc^2",
            text_size=24,
        ),
    )
    page.update()

ft.app(target=main)
```

## Properties

The `Math` control supports the following properties:

### Core Properties
- `tex` (str): The LaTeX formula to render
- `text_color` (ColorValue): Color of the rendered text
- `text_size` (number): Size of the rendered text
- `font_family` (str): Font family for the text
- `font_weight` (FontWeight | str): Weight of the font
- `text_align` (TextAlign): Text alignment
- `selectable` (bool): Whether the text can be selected

### Layout Properties
- `cross_axis_alignment` (CrossAxisAlignment): Cross-axis alignment
- `main_axis_alignment` (MainAxisAlignment): Main-axis alignment

### Control Properties
- `width` (number): Width of the control
- `height` (number): Height of the control
- `expand` (bool): Whether to expand to fill available space
- `opacity` (number): Opacity of the control
- `tooltip` (str): Tooltip text
- `visible` (bool): Whether the control is visible
- `disabled` (bool): Whether the control is disabled

### Animation Properties
- `animate_opacity` (bool): Animate opacity changes
- `animate_position` (bool): Animate position changes
- `animate_scale` (bool): Animate scale changes
- `animate_size` (bool): Animate size changes
- `on_animation_end` (callable): Callback when animation ends
- `rotate` (number): Rotation angle
- `scale` (number): Scale factor
