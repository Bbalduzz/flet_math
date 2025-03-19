import flet as ft
from flet_math import Math

def demo_page():
    # Interactive demo page with input field and preview
    tex_input = ft.TextField(
        label="Input TeX equation here",
        multiline=True,
        min_lines=2,
        max_lines=5,
        border=ft.InputBorder.OUTLINE,
    )
    
    math_output = Math(
        tex="",
        text_size=22,
        text_color=ft.colors.BLUE_500,
        selectable=True,
    )
    
    def update_math(e):
        math_output.tex = tex_input.value
        math_output.update()
    
    tex_input.on_change = update_math
    
    return ft.Column([
        ft.Container(
            padding=10,
            content=tex_input
        ),
        ft.Container(
            padding=10,
            content=ft.Column([
                ft.Text("Flutter Math's output", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                ft.Container(
                    border=ft.border.all(1, ft.colors.BLACK),
                    border_radius=5,
                    padding=10,
                    content=math_output,
                    alignment=ft.alignment.top_center,
                    expand=True,
                )
            ]),
            expand=True,
        )
    ])

def equations_page():
    # Sample equations page
    equations = [
        ["Solution of quadratic equation", r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"],
        ["Schrodinger's equation", r"i\hbar\frac{\partial}{\partial t}\Psi(\vec x,t) = -\frac{\hbar}{2m}\nabla^2\Psi(\vec x,t)+ V(\vec x)\Psi(\vec x,t)"],
        ["Fourier transform", r"\hat f(\xi) = \int_{-\infty}^\infty {f(x)e^{- 2\pi i \xi x}\mathrm{d}x}"],
        ["Maxwell's equations", r'''\left\{\begin{array}{l}
  \nabla\cdot\vec{D} = \rho \\
  \nabla\cdot\vec{B} = 0 \\
  \nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t} \\
  \nabla\times\vec{H} = \vec{J}_f + \frac{\partial\vec{D}}{\partial t} 
\end{array}\right.''']
    ]
    
    equation_cards = []
    for title, tex in equations:
        equation_cards.append(
            ft.Card(
                content=ft.Column([
                    ft.ListTile(
                        title=ft.Text(title),
                        subtitle=ft.Text(tex, selectable=True),
                    ),
                    ft.Container(
                        padding=ft.padding.symmetric(vertical=5, horizontal=15),
                        content=Math(
                            tex=tex,
                            text_size=22,
                            selectable=True,
                        )
                    )
                ])
            )
        )
    
    return ft.ListView(
        controls=[
            ft.Container(
                padding=10,
                content=card
            ) for card in equation_cards
        ],
        expand=True,
    )

def feature_page():
    # Comprehensive list of supported features organized by category
    categories = {
        "Accents": [r"a'", r'\tilde{a}', r"a''", r'\widetilde{ac}', r'\acute{a}', 
                   r'\vec{F}', r'\bar{y}', r'\hat{\theta}', r'\widehat{ac}', r'\ddot{a}'],
        
        "Delimiters": [r'(~)', r'\lparen~\rparen', r'⌈~⌉', r'\lceil~\rceil', 
                      r'[~]', r'\lbrace \rbrace', r'\langle~\rangle', r'\Vert', 
                      r'\left(\LARGE{AB}\right)', r'( \big( \Big( \bigg( \Bigg('],
        
        "Environment": [r'\begin{matrix} a & b \\ c & d \end{matrix}', 
                       r'\begin{pmatrix} a & b \\ c & d \end{pmatrix}', 
                       r'\begin{bmatrix} a & b \\ c & d \end{bmatrix}', 
                       r'\begin{vmatrix} a & b \\ c & d \end{vmatrix}', 
                       r'\begin{cases} a &\text{if } b \\ c &\text{if } d \end{cases}',
                       r'\begin{aligned} a&=b+c \\ d+e&=f \end{aligned}'],
        
        "Greek Letters": [r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta',
                         r'\Gamma', r'\Delta', r'\Theta', r'\Lambda', r'\Xi', r'\Pi', 
                         r'\Sigma', r'\Omega', r'\varepsilon', r'\varphi'],
        
        "Other Characters": [r'\aleph', r'\hbar', r'\imath', r'\nabla', r'\ell',
                            r'\partial', r'\wp', r'\Re', r'\Im', r'\infty'],
        
        "Fractions & Binomials": [r'\frac{a}{b}', r'\tfrac{a}{b}', r'\dfrac{a}{b}', 
                     r'{a \over b}', r'\cfrac{a}{1 + \cfrac{1}{b}}', 
                     r'\binom{n}{k}', r'\dbinom{n}{k}', r'{n\brace k}', r'{n \choose k}'],
        
        "Math Operators": [r'\sin', r'\cos', r'\tan', r'\log', r'\ln', r'\exp',
                          r'\lim_{x \to 0}', r'\det', r'\min', r'\max',
                          r'\int_{a}^{b}', r'\oint', r'\sum_{i=1}^{n}', 
                          r'\prod_{i=1}^{n}', r'\sqrt{x}', r'\sqrt[3]{x}'],
        
        "Big Operators": [r'\sum', r'\prod', r'\coprod', r'\int', r'\iint', r'\iiint',
                         r'\oint', r'\bigcap', r'\bigcup', r'\bigoplus', 
                         r'\bigotimes', r'\bigvee', r'\bigwedge'],
        
        "Binary Operators": [r'+', r'-', r'\times', r'\div', r'\pm', r'\mp',
                            r'\cap', r'\cup', r'\wedge', r'\vee', r'\oplus',
                            r'\otimes', r'\ast', r'\star', r'\circ', r'\bullet'],
        
        "Relations": [r'=', r'\neq', r'<', r'>', r'\leq', r'\geq', 
                     r'\equiv', r'\approx', r'\cong', r'\sim', 
                     r'\subset', r'\supset', r'\subseteq', r'\supseteq', 
                     r'\in', r'\notin', r'\ni', r'\propto'],
        
        "Negated Relations": [r'\neq', r'\ne', r'\not =', r'\not <', r'\not >',
                             r'\not \equiv', r'\not \approx', r'\not \subset',
                             r'\not \supset', r'\notin', r'\notni'],
        
        "Arrows": [r'\leftarrow', r'\rightarrow', r'\Leftarrow', r'\Rightarrow', 
                  r'\leftrightarrow', r'\Leftrightarrow', r'\mapsto', r'\to', 
                  r'\implies', r'\impliedby', r'\iff', 
                  r'\uparrow', r'\downarrow', r'\updownarrow'],
        
        "Extensible Arrows": [r'\xleftarrow{abc}', r'\xrightarrow[under]{over}',
                             r'\xLeftarrow{abc}', r'\xRightarrow{abc}',
                             r'\xleftrightarrow{abc}'],
        
        "Logic & Set Theory": [r'\forall', r'\exists', r'\nexists', 
                             r'\land', r'\lor', r'\neg', r'\implies', r'\iff',
                             r'\emptyset', r'\varnothing', r'\therefore', r'\because'],
        
        "Layout - Annotation": [r'\cancel{5}', r'\bcancel{5}', r'\xcancel{ABC}',
                               r'\overbrace{a+b+c}^{\text{note}}', 
                               r'\underbrace{a+b+c}_{\text{note}}', 
                               r'\boxed{\pi=\frac c d}'],
        
        "Layout - Vertical": [r'x_n', r'e^x', r'_u^o', r'\stackrel{!}{=}', 
                              r'\overset{!}{=}', r'\underset{!}{=}',
                              r'a \atop b', r'\sum_{\substack{0<i<m\\0<j<n}}'],
        
        "Color": [r'\color{blue} F=ma', r'\textcolor{blue}{F=ma}', 
                 r'\textcolor{#228B22}{F=ma}', r'\colorbox{aqua}{A}', 
                 r'\fcolorbox{red}{aqua}{A}'],
        
        "Font": [r'\mathrm{Ab0}', r'\mathbf{Ab0}', r'\mathit{Ab0}', r'\text{Ab0}',
                r'\textbf{Ab0}', r'\textit{Ab0}', r'\textrm{Ab0}',
                r'\mathbb{AB}', r'\mathfrak{AB0}', r'\mathcal{AB0}', 
                r'\mathsf{Ab0}', r'\mathtt{Ab0}'],
        
        "Size": [r'\Huge AB', r'\huge AB', r'\LARGE AB', r'\Large AB', 
                r'\large AB', r'\normalsize AB', r'\small AB', 
                r'\footnotesize AB', r'\scriptsize AB', r'\tiny AB'],
        
        "Style": [r'\displaystyle\sum_{i=1}^n', r'\textstyle\sum_{i=1}^n', 
                 r'\scriptstyle x', r'\scriptscriptstyle x', 
                 r'\lim\limits_x', r'\lim\nolimits_x'],
        
        "Special Notation": [r'\bra{\phi}', r'\ket{\psi}', r'\braket{\phi\vert\psi}',
                            r'\Bra{\phi}', r'\Ket{\psi}'],
        
        "Misc": [r'\dots', r'\cdots', r'\vdots', r'\ddots', 
                r'\LaTeX', r'\TeX', r'\KaTeX', r'\checkmark', 
                r'\dag', r'\dagger', r'\square', r'\triangle', r'\Diamond']
    }
    
    # Create UI for displaying the features
    feature_sections = []
    
    for category, examples in categories.items():
        examples_row = ft.Row(
            controls=[
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Column([
                            ft.Text(example, size=12, selectable=True),
                            ft.Container(height=5),
                            Math(
                                tex=example,
                                text_size=18,
                            )
                        ]),
                        width=180,
                        height=120,
                    ),
                    margin=5,
                ) for example in examples
            ],
            wrap=True,
            scroll=ft.ScrollMode.AUTO
        )
        
        feature_sections.append(
            ft.Column([
                ft.Text(category, size=20, weight=ft.FontWeight.BOLD),
                examples_row,
                ft.Divider(height=20),
            ])
        )
    
    return ft.ListView(
        controls=feature_sections,
        expand=True,
    )

def main(page: ft.Page):
    page.title = "Flet Math Demo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 10
    
    # Create tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Interactive Demo",
                content=demo_page(),
            ),
            ft.Tab(
                text="Equation Samples",
                content=equations_page(),
            ),
            ft.Tab(
                text="Supported Features",
                content=feature_page(),
            ),
        ],
        expand=True,
    )
    
    # Create app bar
    app_bar = ft.AppBar(
        title=ft.Text("Flet Math Demo"),
        center_title=False,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
    )
    
    page.add(app_bar, tabs)
    page.update()

ft.app(target=main)