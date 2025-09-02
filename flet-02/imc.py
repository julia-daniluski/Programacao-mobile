import flet as ft

def main(page: ft.Page):
    # Configuração básica da página
    page.title = "Calculadora IMC"
    page.padding = ft.padding.only(top=48, left=20, right=20, bottom=20)

    # ===================== Temas =====================
    # Tema claro
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background=ft.Colors.WHITE,
            on_background=ft.Colors.BLACK,
        )
    )

    # Tema escuro
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background=ft.Colors.BLACK,
            on_background=ft.Colors.WHITE,
        )
    )

    # Tema inicial
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 550

    # ===================== Funções =====================
    # Fechar banner de aviso
    def close_banner(e):
        page.banner.open = False
        page.update()

    # Alternar tema claro/escuro
    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    # Limpar campos e mensagens de erro
    def limpar_campos(e):
        altura.value = ""
        peso.value = ""
        genero.value = None
        resultado.value = ""
        # Limpar mensagens de erro
        erro_altura.value = ""
        erro_peso.value = ""
        erro_genero.value = ""
        page.update()

    # Calcular IMC com validação de campos obrigatórios
    def calcular_imc(e):
        # Limpa mensagens anteriores
        erro_altura.value = ""
        erro_peso.value = ""
        erro_genero.value = ""
        resultado.value = ""

        campos_validos = True

        # Validação de cada campo
        if not altura.value:
            erro_altura.value = "Preencha sua altura!"
            campos_validos = False
        if not peso.value:
            erro_peso.value = "Preencha seu peso!"
            campos_validos = False
        if genero.value is None:
            erro_genero.value = "Selecione seu gênero!"
            campos_validos = False

        # Atualiza mensagens de erro
        page.update()

        if not campos_validos:
            return  # Para o cálculo se houver campos vazios

        try:
            # Substitui vírgula por ponto para números decimais
            h = float(altura.value.replace(",", "."))
            p = float(peso.value.replace(",", "."))
            imc = p / (h ** 2)
            resultado.value = f"Seu IMC é {imc:.2f}"

            # Classificação do IMC
            if imc < 18.5:
                resultado.value += " (Abaixo do peso)"
            elif imc < 24.9:
                resultado.value += " (Peso normal)"
            elif imc < 29.9:
                resultado.value += " (Sobrepeso)"
            else:
                resultado.value += " (Obesidade)"
        except:
            resultado.value = "Valores inválidos. Use apenas números."

        page.update()

    # ===================== AppBar =====================
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=ft.Colors.DEEP_PURPLE,
        color=ft.Colors.WHITE,
        actions=[
            ft.Row(
                controls=[
                    ft.Text("☼"),
                    ft.Switch(value=False, on_change=alternar_tema),
                    ft.Text("☾"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )

    # ===================== Banner =====================
    page.banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.RED, size=40),
        content=ft.Text("Ops, preencha todos os campos."),
        actions=[ft.TextButton("Ok", on_click=close_banner)],
    )

    # ===================== Campos de Entrada =====================
    altura = ft.TextField(label="Altura (m)", hint_text="Ex: 1.75")
    peso = ft.TextField(label="Peso (kg)", hint_text="Ex: 70")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero",
        options=[ft.dropdown.Option("Masculino"), ft.dropdown.Option("Feminino")],
    )

    # Mensagens de erro específicas
    erro_altura = ft.Text("", color=ft.Colors.RED)
    erro_peso = ft.Text("", color=ft.Colors.RED)
    erro_genero = ft.Text("", color=ft.Colors.RED)

    # Resultado final
    resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)

    # ===================== Layout =====================
    layout = ft.ResponsiveRow(
        controls=[
            # Cada campo + mensagem de erro dentro de um Container
            ft.Container(
                content=ft.Column(controls=[altura, erro_altura]),
                padding=5,
                col={"sm": 12, "md": 6},
            ),
            ft.Container(
                content=ft.Column(controls=[peso, erro_peso]),
                padding=5,
                col={"sm": 12, "md": 6},
            ),
            ft.Container(
                content=ft.Column(controls=[genero, erro_genero]),
                padding=5,
                col={"sm": 12},
            ),
            # Botões
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Calcular IMC",
                            on_click=calcular_imc,
                            bgcolor=ft.Colors.DEEP_PURPLE_900,
                            color=ft.Colors.WHITE,
                        ),
                        ft.OutlinedButton("Limpar", on_click=limpar_campos),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                padding=10,
                col={"sm": 12},
            ),
            # Resultado
            ft.Container(content=resultado, padding=10, col={"sm": 12}),
        ]
    )

    page.add(layout)

# ===================== Inicialização do app =====================
ft.app(target=main)
