from typing import Any, Optional, Union

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.types import ColorValue, TextAlign, FontWeight, CrossAxisAlignment, MainAxisAlignment

class FletMath(ConstrainedControl):
    """
    A control for rendering LaTeX-style mathematical expressions using flutter_math_fork.
    
    Example:
        import flet as ft
        from flet_math import FletMath
        
        def main(page: ft.Page):
            page.add(
                FletMath(
                    tex=r"\\int_0^1 x^2 dx = \\frac{1}{3}",
                    text_color=ft.colors.BLUE_500,
                    text_size=24,
                )
            )
            
        ft.app(main)
    """

    def __init__(
        self,
        #
        # Control
        #
        ref=None,
        width=None,
        height=None,
        expand=None,
        opacity=None,
        tooltip=None,
        visible=None,
        disabled=None,
        data=None,
        #
        # ConstrainedControl
        #
        left=None,
        top=None,
        right=None,
        bottom=None,
        offset=None,
        animate_offset=None,
        animate_position=None,
        animate_scale=None,
        animate_opacity=None,
        animate_size=None,
        on_animation_end=None,
        rotate=None,
        scale=None,
        #
        # FletMath specific
        #
        tex: str = None,
        text_color: Optional[ColorValue] = None,
        text_size: OptionalNumber = None,
        font_family: Optional[str] = None,
        font_weight: Optional[Union[FontWeight, str]] = None,
        text_align: Optional[TextAlign] = None,
        cross_axis_alignment: Optional[CrossAxisAlignment] = None,
        main_axis_alignment: Optional[MainAxisAlignment] = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            expand=expand,
            opacity=opacity,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            offset=offset,
            animate_offset=animate_offset,
            animate_position=animate_position,
            animate_scale=animate_scale,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            on_animation_end=on_animation_end,
            rotate=rotate,
            scale=scale,
        )

        self.tex = tex
        self.text_color = text_color
        self.text_size = text_size
        self.font_family = font_family
        self.font_weight = font_weight
        self.text_align = text_align
        self.cross_axis_alignment = cross_axis_alignment
        self.main_axis_alignment = main_axis_alignment

    def _get_control_name(self):
        return "flet_math"

    # tex
    @property
    def tex(self) -> Optional[str]:
        return self._get_attr("tex")

    @tex.setter
    def tex(self, value: Optional[str]):
        self._set_attr("tex", value)

    # text_color
    @property
    def text_color(self) -> Optional[ColorValue]:
        return self._get_attr("textColor")

    @text_color.setter
    def text_color(self, value: Optional[ColorValue]):
        self._set_attr("textColor", value)

    # text_size
    @property
    def text_size(self) -> OptionalNumber:
        return self._get_attr("textSize")

    @text_size.setter
    def text_size(self, value: OptionalNumber):
        self._set_attr("textSize", value)

    # font_family
    @property
    def font_family(self) -> Optional[str]:
        return self._get_attr("fontFamily")

    @font_family.setter
    def font_family(self, value: Optional[str]):
        self._set_attr("fontFamily", value)

    # font_weight
    @property
    def font_weight(self) -> Optional[Union[FontWeight, str]]:
        return self._get_attr("fontWeight")

    @font_weight.setter
    def font_weight(self, value: Optional[Union[FontWeight, str]]):
        self._set_attr(
            "fontWeight",
            value.value if isinstance(value, FontWeight) else value,
        )

    # text_align
    @property
    def text_align(self) -> Optional[TextAlign]:
        return self._get_attr("textAlign")

    @text_align.setter
    def text_align(self, value: Optional[TextAlign]):
        self._set_attr(
            "textAlign",
            value.value if isinstance(value, TextAlign) else value,
        )

    # cross_axis_alignment
    @property
    def cross_axis_alignment(self) -> Optional[CrossAxisAlignment]:
        return self._get_attr("crossAxisAlignment")

    @cross_axis_alignment.setter
    def cross_axis_alignment(self, value: Optional[CrossAxisAlignment]):
        self._set_attr(
            "crossAxisAlignment",
            value.value if isinstance(value, CrossAxisAlignment) else value,
        )

    # main_axis_alignment
    @property
    def main_axis_alignment(self) -> Optional[MainAxisAlignment]:
        return self._get_attr("mainAxisAlignment")

    @main_axis_alignment.setter
    def main_axis_alignment(self, value: Optional[MainAxisAlignment]):
        self._set_attr(
            "mainAxisAlignment",
            value.value if isinstance(value, MainAxisAlignment) else value,
        )