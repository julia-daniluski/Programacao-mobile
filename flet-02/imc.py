import flet as ft

def main(page: ft.Page):
    # Configuração inicial
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 550

    # Função para fechar o banner
    def close_banner(e):
        page.banner.open = False
        page.update()

    # Função para calcular IMC
    def calcular_imc(e):
        if not altura.value or not peso.value:
            page.banner.open = True
            page.update()
            return

        try:
            h = float(altura.value.replace(",", "."))
            p = float(peso.value.replace(",", "."))
            imc = p / (h ** 2)
            resultado.value = f"Seu IMC é {imc:.2f}"

            # Classificação simples
            if imc < 18.5:
                resultado.value += " (Abaixo do peso)"
            elif imc < 24.9:
                resultado.value += " (Peso normal)"
            elif imc < 29.9:
                resultado.value += " (Sobrepeso)"
            else:
                resultado.value += " (Obesidade)"
        except:
            resultado.value = "Valores inválidos."

        page.update()

    # Alternância entre tema claro e escuro
    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    # AppBar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        actions=[
            ft.Row(
                controls=[
                    ft.Text("🌞"),
                    ft.Switch(value=False, on_change=alternar_tema),
                    ft.Text("🌙"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )

    # Banner de aviso
    page.banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text("Ops, preencha todos os campos."),
        actions=[ft.TextButton("Ok", on_click=close_banner)],
    )

    # Campos de entrada
    altura = ft.TextField(label="Altura (m)", hint_text="Ex: 1.75")
    peso = ft.TextField(label="Peso (kg)", hint_text="Ex: 70")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero",
        options=[ft.dropdown.Option("Masculino"), ft.dropdown.Option("Feminino")],
    )

    # Resultado
    resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)

    # Layout responsivo
    layout = ft.ResponsiveRow(
        controls=[
            ft.Container(content=altura, padding=5, col={"sm": 12, "md": 6}),
            ft.Container(content=peso, padding=5, col={"sm": 12, "md": 6}),
            ft.Container(content=genero, padding=5, col={"sm": 12}),
            ft.Container(
                content=ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
                padding=10,
                col={"sm": 12},
            ),
            ft.Container(content=resultado, padding=10, col={"sm": 12}),
        ],
    )

    page.add(layout)

ft.app(target=main)
